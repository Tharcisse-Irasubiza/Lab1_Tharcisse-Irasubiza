# Lab 1: Grade Evaluator & Archiver
**African Leadership University (ALU)**  
**BSE Year 1 Trimester 2** — *Introduction to Python Programming and Databases*

---

## Submission Deliverables
This repository contains exactly the three required files for the Individual Coding Lab 1 submission:
1. **`grade-evaluator.py`**: The completed Python script for validating grades, computing GPAs, and determining resubmission eligibility.
2. **`organizer.sh`**: The completed Bash script designed to automate workspace archiving and reset the grading environment.
3. **`Readme.md`**: This markdown file, containing clear instructions on how to run both files.

---

## Usage Instructions

### 1. How to Run the Python Application (`grade-evaluator.py`)

The Python application reads a CSV file containing student course grades, validates data integrity, calculates weighted category averages (Formative vs. Summative), calculates GPA, and checks for failed formative assignments eligible for resubmission.

#### Run Command:
Open your terminal inside the project directory and run:
```bash
python3 grade-evaluator.py
(Use python grade-evaluator.py if your system is configured that way).

Execution Steps:
When prompted: Enter the name of the CSV file to process (e.g., grades.csv):, type grades.csv and press Enter.

The script will output:

Validation checks for scores (must be 0−100) and weights (must total exactly 100: Formative = 60, Summative = 40).

Calculated averages for both Formative and Summative categories.

The calculated final GPA based on the formula: GPA=(Total Grade/100)×5.0.

A final standing decision (PASSED or FAILED). Note that passing requires scoring ≥50% in both categories.

Eligible formative assignments for resubmission (if the overall standing is FAILED).

2. How to Run the Shell Script (organizer.sh)
The Bash script automates the archiving of your course data. It moves the active grades.csv to an archive/ folder, renames it with a unique chronological timestamp, creates a fresh template file, and writes a historical log of the process.

Run Commands:
Grant execution permissions to the script (only needs to be done once):

Bash
chmod +x organizer.sh
Execute the script:

Bash
./organizer.sh
Script Actions:
Checks for a directory named archive. If it does not exist, the script creates it automatically.

Renames your current grades.csv by appending a timestamp (e.g., grades_20260715-122400.csv) and moves it into the archive/ folder.

Generates a brand new, empty grades.csv file with standard column headers, preparing your workspace for the next batch of grades.

Appends details of the archival action directly into a file named organizer.log.
