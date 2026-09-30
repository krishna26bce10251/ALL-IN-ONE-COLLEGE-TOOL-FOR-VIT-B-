# Problem Statement and Project Scope

## 1. Problem Statement
As first-semester students at VIT Bhopal, we have to deal with multiple academic regulations and daily hostel expenses manually, which often leads to confusion and calculation mistakes:
- We have a mandatory 75% attendance rule to be eligible for the Final Assessment Test (FAT). Many students do not know exactly how many lectures they can safely bunk without falling below 75%, or how many consecutive classes they must attend back-to-back to recover if they are in the debarred zone.
- Our theory course evaluation follows the rule, consisting of CAT-I (15%), CAT-II (15%), three Digital Assignments (totaling 30%), and the final FAT (40%). In addition, letter grades (S, A, B, C, D, E, F) are awarded using  Relative Grading formulas based on class μ   and Standard Deviation σ . Calculating our scaled internals out of 60, checking if we clear the mandatory 40% FAT cutoff, and estimating our relative grade on paper is complicated.
- We do not have a simple way to figure out what SGPA we need in the next semester to achieve a specific target CGPA for future placement criteria.
- In hostel life, managing our monthly pocket money against daily cafeteria, print shop, and stationery expenses is difficult, often leading to overspending before the month ends.

## 2. Scope of the Project
This project is an all-in-one terminal-based Python utility designed specifically to solve these four everyday student problems in a single program.

The scope includes:
- Evaluating attendance percentages and calculating safe bunks or required recovery lectures.
- Forecasting the next semester's target SGPA based on current CGPA and completed semesters.
- Calculating scaled internal marks out of 60, verifying the 40% FAT passing threshold, and determining relative letter grades using  formulas.
- Logging daily hostel expenses against a fixed monthly budget with warning messages for overdrafts.

The application runs entirely in the Python console using standard  concepts (functions, lists, while loops, and conditional statements) .

## 3. Target Users
-  all years students at VIT Bhopal .
- Hostellers/day scholars who want to monitor their daily pocket money and avoid running out of funds.
-  proctors or teacher  who want to quickly verify attendance eligibility and course performance for their students.

## 4. High-Level Features & Formulas Used
- **Attendance 75% Rule :**
  - Attendance Percentage: `(Attended / Total) * 100`
  - Safe Bunks : `(4 * Attended - 3 * Total) // 3`
  - Classes Needed to recover: `3 * Total - 4 * Attended`
- **Target SGPA Planner:**
  - Formula: `Required_SGPA = (Target_CGPA * Next_Sem) - (Current_CGPA * Completed_Sems)`
- **VIT Exam & Relative Grade Predictor :**
  - Scaled Internals (out of 60): `(CAT1 / 50 * 15) + (CAT2 / 50 * 15) + (DA1 + DA2 + DA3)`
  - Grand Total (out of 100): `Internals + (FAT_Raw / 100 * 40)`
  - Minimum Passing Requirement: Raw FAT marks must be at least 40 out of 100 (`FAT_Raw >= 40`).
  - Relative Grade Cutoffs:
    - S Grade: `Total >= max(90.0, μ + 1.5 * σ)`
    - A Grade: `μ + 0.5 * σ <= Total < μ + 1.5 * σ`
    - B Grade: `μ - 0.5 * σ <= Total < μ + 0.5 * σ`
    - C Grade: `μ - 1.0 * σ <= Total < μ - 0.5 * σ`
    - D Grade: `μ - 1.5 * σ <= Total < μ - 1.0 * σ`
    - E Grade: `μ - 2.0 * σ <= Total < μ - 1.5 * σ`
    - F Grade: `Total < μ - 2.0 * σ` or `FAT_Raw < 40`
- **Hostel Pocket Money Ledger:**
  - Tracks expenses using in-memory list records.
  - Formula: `Remaining_Balance = Monthly_Budget - Total_Spent`
  - Displays instant alerts when expenses exceed the allocated allowance.
- **Interactive Menu:**
  - Simple terminal loop with options 1 to 5 to run and rerun modules easily.