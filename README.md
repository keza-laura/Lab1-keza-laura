# Lab1-keza-laura

Interactive grade generator for Lab 1. Prompts for assignment details
(name, category, grade, weight), calculates weighted totals, final grade
and GPA, shows pass/fail status, and saves the entered assignments to
`grades.csv`.

## Files
- `grade-generator.py`: Interactive script to enter assignments and compute grades.
- `grades.csv`: Output CSV written by `grade-generator.py`.
- `organizer.sh`: Shell script (bash) to archive .csv in archive folder created here with timestamp and appends to organizer.log.
- `README.md`: This file.

## Requirements
- Python 3.x
- Bash shell(Linux or macOs)

## Usage (PowerShell)
Open PowerShell in the project directory and run:

```
python3 .\grade-generator.py
```

Follow the interactive prompts:
- Enter assignment name
- Enter category (`FA` for Formative or `SA` for Summative)
- Enter grade (number between 0 and 100)
- Enter assignment weight (positive number)
When finished, answer `no` to stop adding assignments.

The script prints results (totals, final grade, GPA, status) and writes
`grades.csv` with columns: Assignment, Category, Grade, Weight.

## Notes
- `organizer.sh` is a bash script; run it in WSL or Git Bash on Windows.
- Running `grade-generator.py` will overwrite `grades.csv` in this folder.

## Author
- keza-laura