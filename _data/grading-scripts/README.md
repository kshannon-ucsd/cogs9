# UCSD Grade Processor

A comprehensive tool for processing student grades from Gradescope and Canvas, calculating weighted scores, and generating egrades files for final submission.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Command-Line Options](#command-line-options)
- [Step-by-Step Usage Guide](#step-by-step-usage-guide)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - pandas
  - numpy
  - pyyaml
  - openpyxl (for Excel file support)

## Installation

1. Clone or download this repository to your local machine
2. Install required packages:

```bash
pip install pandas numpy pyyaml openpyxl
```

## File Structure

```
ucsd grades/
├── grade_processor.py     # Main script for all grade processing
├── config.yaml            # Configuration file for real data
├── test-config.yaml       # Configuration for test data
├── gradescope-test.csv    # Sample Gradescope data for testing
├── canvas-test.csv        # Sample Canvas data for testing
└── README.md              # This documentation file
```

## Quick Start

Basic usage with default configuration:

```bash
python grade_processor.py
```

This will:
1. Read configuration from `config.yaml`
2. Process Gradescope and Canvas data files
3. Generate a master grade file
4. Generate an egrades file for submission

## Configuration

The script uses a YAML configuration file to define file paths, column mappings, grading criteria, and more.

### Example Configuration File

```yaml
files:
  canvas: "canvas.csv"          # Path to Canvas CSV/Excel file
  gradescope: "gradescope.csv"  # Path to Gradescope CSV/Excel file
  output: "master.xlsx"         # Path for master output file

column_mappings:
  "PID": "SID"                        # Canvas ID to Gradescope ID mapping
  "NAME": "Name"                      # Name field mapping
  "EMAIL": "Email"                    # Email field mapping
  "R1": "Reading Quiz 1"              # Reading quiz mappings
  "R2": "Reading Quiz 2"
  "R3": "Reading Quiz 3"
  "R4": "Reading Quiz 4"
  "R5": "Reading Quiz 5"
  "A1": "Assignment 1"                # Assignment mappings
  "A2": "Assignment 2"
  "A3": "Assignment 3"
  "F1": "Final Group Project: Part 1" # Final project mappings
  "F2": "Final Group Project: Part 2" # (includes video component)

excluded_columns:
  - "PID"
  - "SID"
  - "Name"
  - "Email"
  - "Sections"

# Threshold hours for late submissions
lateness:
  "Reading Quiz 1": 48
  "Reading Quiz 2": 48
  "Reading Quiz 3": 48
  "Reading Quiz 4": 48
  "Reading Quiz 5": 48
  "Assignment 1": 24
  "Assignment 2": 24
  "Assignment 3": 24
  "Final Group Project: Part 1": 0
  "Final Group Project: Part 2": 0

# Penalty factors: [small penalty, large penalty]
penalties:
  "Reading Quiz 1": [0.5, 1.0]     # 50% / 100% penalties
  "Reading Quiz 2": [0.5, 1.0]
  "Reading Quiz 3": [0.5, 1.0]
  "Reading Quiz 4": [0.5, 1.0]
  "Reading Quiz 5": [0.5, 1.0]
  "Assignment 1": [0.25, 0.5]      # 25% / 50% penalties
  "Assignment 2": [0.25, 0.5]
  "Assignment 3": [0.25, 0.5]
  "Final Group Project: Part 1": [0, 0]  # No late penalties
  "Final Group Project: Part 2": [0, 0]  # No late penalties

# Letter grade cutoffs (percentages)
grade_cutoffs:
  "A+": 97
  "A": 93
  "A-": 90
  "B+": 87
  "B": 83
  "B-": 80
  "C+": 77
  "C": 73
  "C-": 70
  "D+": 67
  "D": 63
  "D-": 60
```

### Configuration Explanation

- **files**: Paths to input and output files
- **column_mappings**: Maps internal column names to Gradescope column names
- **excluded_columns**: Columns to exclude from grade calculations
- **lateness**: Threshold hours for late submissions (before applying large penalty)
- **penalties**: [small_penalty, large_penalty] factors for late submissions
- **grade_cutoffs**: Percentage thresholds for letter grades

## Command-Line Options

The script supports various command-line options for flexibility:

```
usage: grade_processor.py [-h] [--config CONFIG] [--master-only] [--egrades-only] [--test]

Process grades from Gradescope and Canvas

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG, -c CONFIG
                        Path to config file (default: config.yaml)
  --master-only         Only output master file
  --egrades-only        Only output egrades file
  --test                Use test files (gradescope-test.csv and canvas-test.csv)
```

## Step-by-Step Usage Guide

### 1. Prepare Your Data Files

1. Export grades from Gradescope:
   - Go to your Gradescope course
   - Click "Download Grades" (choose CSV format)
   - Save as `gradescope.csv` (or update config file with your filename)

2. Export roster from Canvas:
   - Go to your Canvas course
   - Go to "Grades"
   - Click "Export" (choose CSV format)
   - Save as `canvas.csv` (or update config file with your filename)

### 2. Update Configuration

1. Copy the example configuration or use an existing one
2. Update file paths to match your exported data files
3. Verify column mappings match your Gradescope columns
4. Adjust grade cutoffs and penalties if needed

### 3. Run the Processor

```bash
python grade_processor.py --config your_config.yaml
```

### 4. Review Output Files

1. **Master File**: Contains detailed grade calculations, component scores, and draft grades
2. **Egrades File**: Contains formatted data ready for final grade submission

### 5. Submit Final Grades

Use the generated egrades.csv file to submit final grades according to your institution's process.

## Testing

The script includes built-in test files to verify functionality:

```bash
python grade_processor.py --test
```

This will:
1. Use the test configuration file
2. Process sample data files
3. Generate test output files

## Grading System

This processor uses a 200-point grading system:

- **Reading Quizzes**: 20% (40 points)
  - 5 quizzes, lowest score dropped automatically
  - Each quiz worth 10 points (4 best quizzes count)

- **Assignments**: 30% (60 points)
  - 3 assignments
  - Each assignment worth 20 points
  - **Important**: Assignment 2 and 3 are automatically scaled from 40 points to 20 points if they are worth 40 points in Gradescope

- **Final Project Part 1**: 10% (20 points)

- **Final Project Part 2**: 40% (80 points)
  - Includes the video component (no separate video score)

## Troubleshooting

### Common Issues

1. **Missing Column Error**:
   - Ensure column names in Gradescope match those in your config file
   - If using First Name/Last Name instead of Name, the script will handle it

2. **File Format Issues**:
   - Ensure files are properly formatted CSV or Excel files
   - The script supports both .csv and .xlsx formats

3. **Calculation Errors**:
   - Check that your config file accurately reflects your grading structure
   - Verify lateness penalties are correctly defined
   - Note that Assignment 2 and 3 are automatically scaled if they're worth 40 points

4. **Assignment Scaling**:
   - The script automatically detects if Assignment 2 and 3 are worth 40 points in Gradescope
   - When detected, they are automatically scaled down to 20 points (10% of total grade each)
   - No manual adjustment needed in the configuration file

### Getting Help

For additional help or to report issues, please contact the course administrator.

## File Format Requirements

### Gradescope Export

Must include:
- Student identification (SID or similar)
- Assignment scores
- Assignment max points (script handles scaling A2/A3 from 40 to 20 points)
- Lateness information (in H:M:S format)
- First Name and Last Name columns (or a combined Name column)

### Canvas Export

Must include:
- First Name
- Last Name
- Student ID
- Section ID

## Order of Operations

The processor follows this workflow:

1. Load configuration
2. Read and validate input files
3. Process the master grade file:
   - Map columns from Gradescope to internal format
   - Calculate raw points for each component
   - Apply lateness deductions
   - Calculate adjusted points
   - Compute category scores (readings, assignments, projects)
   - Drop the lowest reading quiz score automatically
   - Scale Assignment 2 and 3 from 40 to 20 points if needed
   - Calculate total points and percentages
   - Assign draft letter grades
4. Generate the egrades file:
   - Extract required columns from Canvas
   - Merge with letter grades from master file
   - Format for submission
5. Save output files