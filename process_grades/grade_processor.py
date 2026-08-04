#!/usr/bin/env python3
"""COGS 9 grade processor.

Turns a Gradescope export + a Canvas roster into finalized grades and an
eGrades upload file, applying the scheme defined in a YAML config (curve,
free points, per-assignment point reductions, drop-lowest quiz).

Two inputs (named in the config):
  - Gradescope export  (.csv or .xlsx)
  - Canvas roster CSV  (columns: Last Name, First Name, Student ID,
                        Section ID, Current Grade, Final Assigned eGrade)

Two outputs (written only in real-run mode):
  1. <canvas>_finalized.csv : the Canvas roster with Current Grade (%) and
     Final Assigned eGrade (letter) filled in.
  2. <egrades_out>          : eGrades upload, CSV delimited, header exactly
     "Last Name,First Name,Student ID,SectionId,Final_Assigned_Egrade".

Usage (from inside process_grades/):
  pixi run dry-run     # print the full breakdown, write nothing
  pixi run run         # write both CSVs
or directly:
  python grade_processor.py --config config.yaml [--dry-run]
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import sys
from collections import Counter


# Percent floors -> letter (used if the config omits grade_scale).
DEFAULT_SCALE = {
    "A+": 97, "A": 93, "A-": 90,
    "B+": 87, "B": 83, "B-": 80,
    "C+": 77, "C": 73, "C-": 70,
    "D": 60, "F": 0,
}


# ------------------------------- helpers ---------------------------------- #

def norm_sid(value) -> str:
    """Normalize a student ID for matching (strip spaces, uppercase)."""
    return str(value if value is not None else "").strip().upper()


def to_float(value, default=0.0) -> float:
    if value is None:
        return default
    text = str(value).strip()
    if text == "":
        return default
    try:
        return float(text)
    except ValueError:
        return default


def trunc2(value) -> float:
    """Truncate to 2 decimals (never rounds up, per the syllabus)."""
    return math.floor(value * 100) / 100.0


def find_col(fieldnames, *candidates):
    """Case/space-insensitive lookup of a column name; returns the real name."""
    def key(s):
        return "".join(str(s).lower().split())
    wanted = {key(c) for c in candidates}
    for name in fieldnames:
        if key(name) in wanted:
            return name
    return None


# --------------------------- config / inputs ------------------------------ #

def load_config(path):
    try:
        import yaml
    except ImportError:  # pragma: no cover
        sys.exit("PyYAML is required. Run inside pixi:  pixi run dry-run")
    if not os.path.exists(path):
        sys.exit(f"Config not found: {path}")
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def load_gradescope(path):
    """Return a list of row dicts keyed by the export's column headers."""
    if not os.path.exists(path):
        sys.exit(f"Gradescope export not found: {path}")
    ext = os.path.splitext(path)[1].lower()
    if ext in (".xlsx", ".xls"):
        return _read_xlsx(path)
    with open(path, newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def _read_xlsx(path):
    try:
        import openpyxl
    except ImportError:  # pragma: no cover
        sys.exit("openpyxl is required to read .xlsx. Run inside pixi.")
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    sheet = workbook.active
    rows_iter = sheet.iter_rows(values_only=True)
    header = ["" if h is None else str(h) for h in next(rows_iter)]
    rows = []
    for raw in rows_iter:
        rows.append({header[i]: ("" if v is None else v) for i, v in enumerate(raw)})
    return rows


def index_reductions(cfg):
    """{sid: {assignment: total_points_reduced}} from the reductions list."""
    out = {}
    for entry in (cfg.get("reductions") or []):
        sid = norm_sid(entry["sid"])
        assignment = entry["assignment"]
        pts = to_float(entry["points"])
        out.setdefault(sid, {}).setdefault(assignment, 0.0)
        out[sid][assignment] += pts
    return out


def index_free_points(cfg):
    """{sid: total_free_points} from the free_points map."""
    out = {}
    for sid, pts in (cfg.get("free_points") or {}).items():
        key = norm_sid(sid)
        out[key] = out.get(key, 0.0) + to_float(pts)
    return out


# ---------------------------- computation --------------------------------- #

def score_and_max(row, assignment):
    if assignment not in row:
        sys.exit(f"Gradescope export has no column named '{assignment}'. "
                 f"Check the 'categories' names in the config.")
    score = to_float(row.get(assignment))
    maximum = to_float(row.get(f"{assignment} - Max Points"))
    return score, maximum


def compute_student(row, cfg, reductions_by_sid, free_by_sid, scale):
    cats = cfg["categories"]
    sid = norm_sid(row.get("SID"))
    reductions = reductions_by_sid.get(sid, {})

    def adjusted(assignment):
        score, maximum = score_and_max(row, assignment)
        score = max(0.0, score - reductions.get(assignment, 0.0))
        return score, maximum

    earned = 0.0
    possible = 0.0

    for assignment in cats["assignments"]["columns"]:
        score, maximum = adjusted(assignment)
        earned += score
        possible += maximum

    quiz_cfg = cats["quizzes"]
    drop = int(quiz_cfg.get("drop_lowest", 0) or 0)
    quizzes = [(*adjusted(a), a) for a in quiz_cfg["columns"]]
    quizzes.sort(key=lambda item: item[0])          # lowest score first
    dropped = quizzes[:drop] if drop else []
    for score, maximum, _name in quizzes[drop:]:
        earned += score
        possible += maximum

    for assignment in cats["project"]["columns"]:
        score, maximum = adjusted(assignment)
        earned += score
        possible += maximum

    free = free_by_sid.get(sid, 0.0)
    earned += free

    raw_pct = (earned / possible * 100.0) if possible else 0.0
    curve = to_float(cfg.get("curve_percent"))
    final_pct = trunc2(raw_pct + curve)

    return {
        "sid": sid,
        "first": str(row.get("First Name", "")).strip(),
        "last": str(row.get("Last Name", "")).strip(),
        "earned": earned,
        "possible": possible,
        "free": free,
        "raw_pct": raw_pct,
        "curve": curve,
        "final_pct": final_pct,
        "letter": letter_for(final_pct, scale),
        "dropped": [name for _s, _m, name in dropped],
    }


def letter_for(pct, scale):
    for letter, floor in sorted(scale.items(), key=lambda kv: kv[1], reverse=True):
        if pct >= floor:
            return letter
    # Fall back to the lowest-floor letter.
    return min(scale.items(), key=lambda kv: kv[1])[0]


# ------------------------------ outputs ----------------------------------- #

EGRADES_HEADER = ["Last Name", "First Name", "Student ID", "SectionId",
                  "Final_Assigned_Egrade"]


def resolve_canvas_columns(fieldnames):
    cols = {
        "id": find_col(fieldnames, "Student ID", "SID", "PID"),
        "last": find_col(fieldnames, "Last Name"),
        "first": find_col(fieldnames, "First Name"),
        "section": find_col(fieldnames, "Section ID", "SectionId", "Section"),
        "current": find_col(fieldnames, "Current Grade"),
        "letter": find_col(fieldnames, "Final Assigned eGrade",
                           "Final Assigned Egrade", "Final_Assigned_Egrade"),
    }
    missing = [k for k, v in cols.items() if v is None]
    if missing:
        sys.exit("Canvas roster is missing expected column(s): "
                 + ", ".join(missing) + f"\nFound columns: {fieldnames}")
    return cols


def load_canvas(path):
    if not os.path.exists(path):
        sys.exit(f"Canvas roster not found: {path}")
    with open(path, newline="", encoding="utf-8-sig") as handle:
        sample = handle.read(8192)
        handle.seek(0)
        delimiter = "\t" if sample.count("\t") > sample.count(",") else ","
        reader = csv.DictReader(handle, delimiter=delimiter)
        rows = list(reader)
        return reader.fieldnames, rows, delimiter


def build(cfg):
    """Do all the work; return (canvas_fieldnames, canvas_cols, canvas_rows,
    matched, results, warnings, delimiter)."""
    scale = cfg.get("grade_scale") or DEFAULT_SCALE
    files = cfg.get("files", {})
    reductions = index_reductions(cfg)
    free = index_free_points(cfg)

    gs_rows = load_gradescope(files["gradescope"])
    results = {}
    for row in gs_rows:
        res = compute_student(row, cfg, reductions, free, scale)
        if res["sid"]:
            results[res["sid"]] = res

    fieldnames, canvas_rows, delimiter = load_canvas(files["canvas"])
    cols = resolve_canvas_columns(fieldnames)

    matched, unmatched_roster = [], []
    for row in canvas_rows:
        sid = norm_sid(row.get(cols["id"]))
        res = results.get(sid)
        if res:
            row[cols["current"]] = f"{res['final_pct']:.2f}"
            row[cols["letter"]] = res["letter"]
            matched.append((row, res))
        else:
            row[cols["current"]] = ""
            row[cols["letter"]] = ""
            unmatched_roster.append(row)

    roster_sids = {norm_sid(r.get(cols["id"])) for r in canvas_rows}
    unmatched_gs = [res for sid, res in results.items() if sid not in roster_sids]

    warnings = []
    for row in unmatched_roster:
        warnings.append("In roster but NOT in Gradescope: "
                        f"{norm_sid(row.get(cols['id']))} "
                        f"({row.get(cols['last'])}, {row.get(cols['first'])})")
    for res in unmatched_gs:
        warnings.append("In Gradescope but NOT in roster: "
                        f"{res['sid']} ({res['last']}, {res['first']})")

    return fieldnames, cols, canvas_rows, matched, results, warnings, delimiter


def write_outputs(cfg, fieldnames, cols, canvas_rows, matched, delimiter):
    files = cfg["files"]
    canvas_path = files["canvas"]
    finalized = files.get("finalized_out") or (
        os.path.splitext(canvas_path)[0] + "_finalized.csv")
    egrades = files["egrades_out"]
    for out_path in (finalized, egrades):
        parent = os.path.dirname(out_path)
        if parent:
            os.makedirs(parent, exist_ok=True)

    with open(finalized, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(canvas_rows)

    with open(egrades, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)  # CSV delimited, per eGrades spec
        writer.writerow(EGRADES_HEADER)
        for row, res in matched:
            writer.writerow([
                row.get(cols["last"]),
                row.get(cols["first"]),
                row.get(cols["id"]),
                row.get(cols["section"]),
                res["letter"],
            ])
    return finalized, egrades


# ---------------------------- dry-run report ------------------------------ #

def print_report(cfg, cols, matched, results, warnings):
    reductions = cfg.get("reductions") or []
    free = cfg.get("free_points") or {}
    curve = to_float(cfg.get("curve_percent"))
    drop = int((cfg.get("categories", {}).get("quizzes", {}) or {}).get("drop_lowest", 0) or 0)

    print("=" * 72)
    print("DRY RUN - no files will be written.")
    print("=" * 72)
    print(f"Curve: +{curve:g}%   |   Quizzes: drop lowest {drop}   |   "
          f"Gradescope students: {len(results)}   |   Roster matched: {len(matched)}")

    if reductions:
        print("\nPoint reductions applied:")
        for r in reductions:
            print(f"  {norm_sid(r['sid']):<10} {r['assignment']:<28} -{to_float(r['points']):g}")
    if free:
        print("\nFree points applied (to total):")
        for sid, pts in free.items():
            print(f"  {norm_sid(sid):<10} +{to_float(pts):g}")

    print("\nStudents:")
    print(f"  {'SID':<10} {'Name':<24} {'Earned/Poss':>13} {'Raw%':>7} "
          f"{'Curve':>6} {'Final%':>7}  {'Ltr':<3}")
    for row, res in sorted(matched, key=lambda m: (m[1]["last"], m[1]["first"])):
        name = f"{res['last']}, {res['first']}"[:24]
        ep = f"{res['earned']:.1f}/{res['possible']:.0f}"
        print(f"  {res['sid']:<10} {name:<24} {ep:>13} {res['raw_pct']:>7.2f} "
              f"{'+' + format(res['curve'], 'g'):>6} {res['final_pct']:>7.2f}  {res['letter']:<3}")

    dist = Counter(res["letter"] for _row, res in matched)
    order = list(cfg.get("grade_scale", DEFAULT_SCALE).keys())
    print("\nLetter distribution: " + "  ".join(
        f"{ltr}:{dist[ltr]}" for ltr in order if dist[ltr]))

    if warnings:
        print(f"\n!! {len(warnings)} warning(s) - resolve before uploading:")
        for w in warnings:
            print(f"  - {w}")
    else:
        print("\nNo mismatches between Gradescope and the roster.")

    files = cfg["files"]
    finalized = files.get("finalized_out") or (
        os.path.splitext(files["canvas"])[0] + "_finalized.csv")
    print("\nWould write:")
    print(f"  {finalized}   ({len(matched)} graded, "
          f"{len(matched)} of roster filled)")
    print(f"  {files['egrades_out']}   ({len(matched)} rows, CSV)")


# -------------------------------- main ------------------------------------ #

def main():
    parser = argparse.ArgumentParser(description="COGS 9 grade processor")
    parser.add_argument("--config", default="config.yaml",
                        help="path to the YAML config (default: config.yaml)")
    parser.add_argument("--dry-run", action="store_true",
                        help="print the breakdown and write nothing")
    args = parser.parse_args()

    cfg = load_config(args.config)

    # Safety: an output must never overwrite one of the input files.
    fpaths = cfg.get("files", {})
    inputs = {os.path.abspath(fpaths[k]) for k in ("gradescope", "canvas") if fpaths.get(k)}
    fin = fpaths.get("finalized_out") or (
        os.path.splitext(fpaths.get("canvas", ""))[0] + "_finalized.csv")
    for label, path in (("finalized_out", fin), ("egrades_out", fpaths.get("egrades_out"))):
        if path and os.path.abspath(path) in inputs:
            sys.exit(f"Config error: {label} ('{path}') is one of your input files.\n"
                     f"Give it a distinct name, e.g. egrades_out: data/<session>/egrades.csv")

    fieldnames, cols, canvas_rows, matched, results, warnings, delimiter = build(cfg)

    if args.dry_run:
        print_report(cfg, cols, matched, results, warnings)
        return

    finalized, egrades = write_outputs(
        cfg, fieldnames, cols, canvas_rows, matched, delimiter)
    print(f"Wrote {finalized} ({len(canvas_rows)} rows).")
    print(f"Wrote {egrades} ({len(matched)} rows).")
    if warnings:
        print(f"\n!! {len(warnings)} warning(s):")
        for w in warnings:
            print(f"  - {w}")
        print("Review these before uploading to eGrades.")


if __name__ == "__main__":
    main()
