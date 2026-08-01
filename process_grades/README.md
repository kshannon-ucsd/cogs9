# COGS 9 grade processing

Turns a **Gradescope export** + a **Canvas roster** into finalized grades and an
**eGrades** upload file, driven by a per-session YAML config.

Real student data and generated exports live under `data/` and are gitignored;
only the tooling and sanitized samples are tracked.

## Setup (once)

Uses [pixi](https://pixi.sh) for the Python environment:

    cd process_grades
    pixi install

## Per session

Each session has its own data folder, config, and tasks:

| Session | Folder | Config | Tasks |
|--|--|--|--|
| Summer 1 | `data/summer_1_26/` | `config.summer_1_26.yaml` | `pixi run s1-dry` / `s1-run` |
| Summer 2 | `data/summer_2_26/` | `config.summer_2_26.yaml` | `pixi run s2-dry` / `s2-run` |

1. Drop the two exports into that session's folder, named `gradescope.csv` and
   `canvas.csv` (or edit the `files:` paths in the config).
2. Set `curve_percent`, `free_points`, `reductions` in that session's config.
3. Preview, then generate:

       pixi run s1-dry     # prints the breakdown + warnings, writes nothing
       pixi run s1-run     # writes the exports into data/summer_1_26/

Always `s1-dry`/`s2-dry` first and read the warnings (unmatched students, etc.)
before the real run. `pixi run demo` dry-runs against the checked-in samples.

## Outputs (into the session folder)

1. `canvas_finalized.csv`: the roster with **Current Grade** (%) and
   **Final Assigned eGrade** (letter) filled in.
2. `egrades.csv`: the eGrades upload (CSV), header
   `Last Name,First Name,Student ID,SectionId,Final_Assigned_Egrade`.

## Grading (200 pts, per the syllabus)

| Category | Columns | Points |
|--|--|--|
| Assignments | Assignment 1-3 | 20 each = 60 |
| Reading quizzes (drop lowest 1) | Reading Quiz 1-5 | best 4 x 10 = 40 |
| Final project | Part 1 (20) + Part 2 (40) + Video (40) | 100 |

- Blank score = 0; max points come from the export's `- Max Points` columns.
- Lateness is **not** auto-penalized; use `reductions` for late deductions.
- Students match on ID as a case-insensitive string (Gradescope `SID` vs Canvas `Student ID`).
- Final % is truncated to 2 decimals; letters use the standard scale (no D+/D-).

## Files here

Tracked: `grade_processor.py`, `pixi.toml`, `config.example.yaml`, `*.sample.csv`,
`data/summer_*_26/.gitkeep`, this README.
Gitignored: the per-session configs, anything you drop in `data/`, generated exports, `.pixi/`.
