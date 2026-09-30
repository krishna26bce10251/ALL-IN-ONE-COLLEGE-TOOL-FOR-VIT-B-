# ALL IN ONE COLLEGE TOOL FOR VIT-B STUDENTS

## Overview
As first-semester engineering students at VIT Bhopal, we found ourselves repeatedly doing manual calculations for our 75% attendance policy, our theory internal weightages, target GPAs, and monthly pocket money. We built this terminal tool using basic Python concepts learned in our coursework so any student can check these details in seconds without making math errors.

## Features & Academic Formulas

### 1. Attendance & 75% Rule Assistant
- Tells you your exact attendance percentage and whether you are safe or debarred.
- **Safe Bunks (when >= 75%):** `int((4 * Attended - 3 * Total) / 3)`
- **Recovery Lectures Needed (when < 75%):** `3 * Total - 4 * Attended`

### 2. Next Semester Target SGPA Planner
- Helps you figure out what SGPA you must score in the upcoming semester to reach your dream CGPA.
- **Formula:** `Required_SGPA = (Target_CGPA * Next_Sem) - (Current_CGPA * Completed_Sems)`

### 3. VIT Bhopal Exam Evaluation & Relative Grade Predictor
- Scales course marks strictly according to official Table-3 Theory Course weightages:
  - CAT-I: 50 Marks (scaled to 15%)
  - CAT-II: 50 Marks (scaled to 15%)
  - Digital Assignments: 3 assignments of 10 marks each = 30 Marks
  - Final Assessment Test (FAT): 100 Marks (scaled to 40%)
- Enforces the mandatory passing threshold: raw FAT marks must be at least 40 out of 100.
- Predicts course letter grades using Table-5 Relative Grading formulas based on class Mean (μ) and Standard Deviation (σ):
  - **S Grade:** `Total >= max(90.0, μ + 1.5 * σ)`
  - **A Grade:** `μ + 0.5 * σ <= Total < μ + 1.5 * σ`
  - **B Grade:** `μ - 0.5 * σ <= Total < μ + 0.5 * σ`
  - **C Grade:** `μ - 1.0 * σ <= Total < μ - 0.5 * σ`
  - **D Grade:** `μ - 1.5 * σ <= Total < μ - 1.0 * σ`
  - **E Grade:** `μ - 2.0 * σ <= Total < μ - 1.5 * σ`
  - **F Grade:** `Total < μ - 2.0 * σ` or `FAT < 40`

### 4. Hostel Pocket Money & Daily Expense Log
- Sets a monthly pocket money allowance.
- Logs daily expenses with item descriptions (e.g., canteen snacks, printing, stationery).
- Displays running balance and prints a warning alert if you exceed your monthly budget.

## Technologies/Tools Used
- **Programming Language:** Python 3.x
- **Core Tools:** Python Standard Library (no third-party dependencies required), Git, and GitHub
- **Python Concepts Applied:** User-defined functions (`def attendance`, `def cgpa_target`, `def evaluator`, `def budget`, `def main`), conditional branching (`if-elif-else`), loops (`while`), input/output (`input()`, `print()`), and list data structures (`expense_names`, `expense_amounts`).

## How to Run the Project
1. Download or clone the project folder from GitHub.
2. Open your terminal or Command Prompt inside the project folder.
3. Run the following command to start the application:
```bash
   python main.py 
```
                 

#### Instructions for Testing
To test the application interactively in your terminal, launch `main.py` and run the following validated test cases:
1. **Attendance Check:** Enter `33` conducted and `31` attended lectures; confirm the system calculates `93.94%` attendance and permits `8` safe bunks while remaining eligible.
2. **Target SGPA Planner:** Select Option 2, enter current CGPA `8.0`, completed semesters `2`, and target CGPA `8.5`; confirm that the required next semester SGPA evaluates to `9.5`.
3. **Exam Scaling & Relative Grade:** Select Option 3, enter CAT-I `38`, CAT-II `40`, and DAs `10, 10, 8` (Internal = `51.4 / 60`), enter expected FAT `80`, and press Enter for default class statistics (Mean 60, Sigma 10); confirm the assigned grade evaluates to `A` (9 grade points).
4. **Hostel Expense Log:** Set a monthly budget of `500`, record an expense of `50` for `chips`, and verify that the remaining balance displays `450`.