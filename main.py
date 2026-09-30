# ==========================================================
# Project Title : ALL IN ONE COLLEGE TOOL FOR VIT - B STUDENTS
# Course: INTRODUCTION TO PLOBLEM SOLVING
# NAME : KRISHNA GAUTAM
# REG.NO : 26BCE10251
# ==========================================================

#Hostel Pocket Money containers
expense_names = []
expense_amounts = []
monthly_budget = 0
total_spent = 0


# ==========================================================
# MODULE 1: HOW MANY CLASSES STUDENT CAN BUNK SATYING ABOVE 75%/CLASSES TO ATTEND TO STAY ABOVE 75 %
            
# ==========================================================

def attendance():
    print("\n--- HOW MANY CLASSES STUDENT CAN BUNK SATYING ABOVE 75%/CLASSES TO ATTEND TO STAY ABOVE 75 % ---")
    total_str = input("Enter total lectures conducted till today: ").strip()
    attended_str = input("Enter lectures you attended: ").strip()

    if not total_str.isdigit() or not attended_str.isdigit():
        print("Please enter valid positive whole numbers.")
        return

    total = int(total_str)
    attended = int(attended_str)

    if total == 0:
        print("Total conducted lectures cannot be zero.")
        return

    if attended > total:
        print("Attended lectures cannot exceed total conducted lectures!")
        return

    atd_per = (attended / total) * 100.0
    print("Your Current Attendance: " + str(round(atd_per, 2)) + "%")

    if atd_per >= 75.0:
        # Safe bunks classes : (4*attended - 3*total) // 3
        bunks = int((4 * attended - 3 * total) / 3)
        print("Status: ELIGIBLE (Safe to sit/apppear for TEE)")
        print("You can safely bunk " + str(bunks) + " more lecture(s) while staying >= 75%.")
    else:
        # Recovery to get above 75%: 3*total - 4*attended
        needed = (3 * total) - (4 * attended)
        print("Status: DEBARRED WARNING (Below 75%)")
        print("You must attend " + str(needed) + " consecutive lecture(s) without bunking to reach 75%.")


# ==========================================================
# MODULE 2: NEXT SEMESTER TARGET SGPA & CGPA TARGET SETTER 
# ==========================================================

def cgpa_target():
    print("\n--- Target SGPA & CGPA SETTER FOR NEXT SEM ---")
    curr = input("Enter current CGPA (e.g., 7.5): ").strip()
    semester = input("Enter completed semesters (e.g., 1): ").strip()
    tar = input("Enter target overall CGPA: ").strip()

    try:
        current = float(curr)
        sems = int(semester)
        target = float(tar)
    except ValueError:
        print("Invalid input! Use decimal numbers for CGPA and integers for semesters.")
        return

    if sems < 1:
        print("Semesters completed must be at least 1.")
        return

    next_sem = sems + 1
    # Formula: Required SGPA = (Target * NextSem) - (CurrentCGPA * CompletedSems)
    needed_sgpa = (target * next_sem) - (current * sems)
    needed_sgpa = round(needed_sgpa, 2)

    print("Target Overall CGPA: " + str(target))
    if needed_sgpa > 10.0:
        print("Required SGPA: " + str(needed_sgpa))
        print("Result: Not mathematically achievable in one semester (Max SGPA is 10.0).")
    elif needed_sgpa <= 0:
        print("Result: You are safely above target! Just clear all upcoming courses.")
    else:
        print("Result: You must secure at least " + str(needed_sgpa) + " SGPA in the next semester.")


# ==========================================================
# MODULE 3:  EXAM EVALUATION & RELATIVE GRADE PREDICTOR
# Scheme: CAT-1 (15%), CAT-2 (15%), DA 3x10 (30%), FAT (40%)
# Relative Grading using Class Mean & standard deviation
# ==========================================================

def evaluator():
    print("\n--- VIT Bhopal Exam Weightage & Relative Grade Predictor ---")
    print("Weightage Structure:")
    print("  CAT-I: 50 Marks (Scaled to 15%)")
    print("  CAT-II: 50 Marks (Scaled to 15%)")
    print("  Digital Assignments (3 x 10): 30 Marks")
    print("  Final Assessment Test (FAT): 100 Marks (Scaled to 40%)")
    print("-----------------------------------------------------")

    c1 = input("Enter CAT-I marks (out of 50): ").strip()
    c2 = input("Enter CAT-II marks (out of 50): ").strip()
    da1 = input("Enter Digital Assignment 1 marks (out of 10): ").strip()
    da2 = input("Enter Digital Assignment 2 marks (out of 10): ").strip()
    da3 = input("Enter Digital Assignment 3 marks (out of 10): ").strip()

    try:
        cat1 = float(c1)
        cat2 = float(c2)
        d1 = float(da1)
        d2 = float(da2)
        d3 = float(da3)
    except ValueError:
        print("Error: Please enter valid numbers for marks.")
        return

    if cat1 > 50 or cat2 > 50 or d1 > 10 or d2 > 10 or d3 > 10:
        print("Input out of range! CATs are out of 50 and DAs are out of 10.")
        return

    cat1_weight = (cat1 / 50.0) * 15.0
    cat2_weight = (cat2 / 50.0) * 15.0
    da_total = d1 + d2 + d3
    total_internals = cat1_weight + cat2_weight + da_total

    print("\n>> Internal Marks Secured: " + str(round(total_internals, 2)) + " / 60")
    print("Minimum FAT Score Needed Just to Pass: 40.0 / 100")

    print("\n--- Predict Your Final Course Grade (Relative Grading) ---")
    fat_input = input("Enter your expected or scored FAT marks (out of 100): ").strip()
    try:
        raw_fat = float(fat_input)
    except ValueError:
        print("Invalid FAT marks entered.")
        return

    if raw_fat < 0 or raw_fat > 100:
        print("FAT score must be between 0 and 100.")
        return

    fat_weight = (raw_fat / 100.0) * 40.0
    grand_total = total_internals + fat_weight

    print("\n------------- SCORE BREAKDOWN -------------")
    print("Internal Contribution (CATs + DA): " + str(round(total_internals, 2)) + " / 60")
    print("FAT Contribution:                  " + str(round(fat_weight, 2)) + " / 40")
    print("Grand Total Marks:                 " + str(round(grand_total, 2)) + " / 100")

    print("\n[Optional: Class Statistics for Relative Grading]")
    mean_in = input("Enter class Mean (press Enter for default 60): ").strip()
    sigma_in = input("Enter class Sigma / Std Dev (press Enter for default 10): ").strip()

    mean = float(mean_in) if mean_in != "" else 60.0
    sigma = float(sigma_in) if sigma_in != "" else 10.0

    s_cutoff = max(90.0, mean + 1.5 * sigma)
    a_cutoff = mean + 0.5 * sigma
    b_cutoff = mean - 0.5 * sigma
    c_cutoff = mean - 1.0 * sigma
    d_cutoff = mean - 1.5 * sigma
    e_cutoff = mean - 2.0 * sigma

    print("\n------------- FINAL GRADE ASSIGNMENT -------------")
    if raw_fat < 40.0:
        print("Assigned Grade: F (Fail)")
        print("Grade Points:   0")
        print("Reason: Failed mandatory individual FAT threshold (Score was < 40/100).")
    elif grand_total >= s_cutoff:
        print("Assigned Grade: S (Outstanding)")
        print("Grade Points:   10")
    elif grand_total >= a_cutoff:
        print("Assigned Grade: A (Excellent)")
        print("Grade Points:   9")
    elif grand_total >= b_cutoff:
        print("Assigned Grade: B (Very Good)")
        print("Grade Points:   8")
    elif grand_total >= c_cutoff:
        print("Assigned Grade: C (Good)")
        print("Grade Points:   7")
    elif grand_total >= d_cutoff:
        print("Assigned Grade: D (Average)")
        print("Grade Points:   6")
    elif grand_total >= e_cutoff:
        print("Assigned Grade: E (Pass)")
        print("Grade Points:   4")
    else:
        print("Assigned Grade: F (Fail)")
        print("Grade Points:   0")
        print("Reason: Total aggregate score is below passing cutoff.")
    print("--------------------------------------------------")


# ==========================================================
# MODULE 4:  POCKET MONEY & EXPENSE TRACKER
# ==========================================================

def budget():
    global monthly_budget, total_spent, expense_names, expense_amounts

    while True:
        balance = monthly_budget - total_spent
        print("\n--- Hostel Budget & Expense Log ---")
        print("Monthly Pocket money: Rs. " + str(monthly_budget))
        print("Total Expended:    Rs. " + str(total_spent))
        print("Remaining Balance: Rs. " + str(balance))
        print("-----------------------------------")
        print("1. Set / Update Monthly Pocket money")
        print("2. Add Expense (Canteen, Printing, other)")
        print("3. View Detailed Expense Log")
        print("4. Return to Main Menu")

        opt = input("Enter choice (1-4): ").strip()

        if opt == "1":
            pm_str = input("Enter your monthly pocket money amount (Rs.): ").strip()
            if pm_str.isdigit():
                monthly_budget = int(pm_str)
                print("monthly budget updated successfully.")
            else:
                print("Please enter a valid whole number.")

        elif opt == "2":
            desc = input("Expense description: ").strip()
            cost_str = input("Amount spent (Rs.): ").strip()
            if cost_str.isdigit() and desc != "":
                cost = int(cost_str)
                expense_names.append(desc)
                expense_amounts.append(cost)
                total_spent = total_spent + cost
                print("Recorded: " + desc + " (-Rs. " + str(cost) + ")")

                if (monthly_budget - total_spent) < 0:
                    print("** WARNING: You have exceeded your monthly allowance! **")
            else:
                print("Invalid input. Description cannot be empty and amount must be numeric.")

        elif opt == "3":
            print("\n--- Expense History ---")
            if len(expense_names) == 0:
                print("No expenses recorded yet.")
            else:
                for i in range(len(expense_names)):
                    print(str(i + 1) + ". " + expense_names[i] + " -> Rs. " + str(expense_amounts[i]))

        elif opt == "4":
            break
        else:
            print("Invalid choice, select between 1 and 4.")


# ==========================================================
# MAIN APPLICATION LOOP
# ==========================================================

def main():
    while True:
        print("\n==============================================")
        print("   ALL IN ONE COLLEGE TOOL FOR VIT- B STUDENTS  ")
        print("==============================================")
        print("1. HOW MANY CLASSES STUDENT CAN BUNK SATYING ABOVE 75%/CLASSES TO ATTEND TO STAY ABOVE 75 %")
        print("2. Next Semester SGPA Target SETTER")
        print("3. EXAM EVALUATION, TEE GOAL & GRADE PREDICTOR")
        print("4. Pocket Money & Daily Expense Log")
        print("5. Exit Application")

        selection = input("\nEnter choice (1-5): ").strip()

        if selection == "1":
            attendance()
        elif selection == "2":
            cgpa_target()
        elif selection == "3":
            evaluator()
        elif selection == "4":
            budget()
        elif selection == "5":
            print("\nThank you for using the ALL IN ONE COLLEGE TOOL. Good luck with your semester!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
