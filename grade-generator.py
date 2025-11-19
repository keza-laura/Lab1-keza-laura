#!/usr/bin/env python3
import csv

"""
Collection and validation of information like assignment name, cat(category
weight, and grades
"""
arr = []   # Stores all assignments as dictionaries

def info():

    Aname = input("Enter assignment name: ")

    # Category validation
    while True:
        cat = input("Enter category (FA for Formative, SA for Summative: ").upper()
        if cat not in ["FA", "SA"]:
            print("Invalid category! Please type FA or SA.")
        else:
            break

    # Grade validation
    while True:
        try:
            grade = float(input("Enter grade (0 - 100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")

    # Weight validation
    while True:
        try:
            weight = float(input("Enter assignment weight: "))
            if weight > 0:
                break
            else:
                print("Weight must be a positive number.")
        except ValueError:
            print("Invalid input. Enter a number.")
        #calcutation and display of grades out of the given weight.
    weighted_grade = (grade / 100) * weight
    print(f"Weighted Grade: {weighted_grade}")

    # Add data to array
    info = {
        "name": Aname,
        "category": cat,
        "grade": grade,
        "weight": weight
    }

    arr.append(info)


# MAIN LOOP
while True:
    info()
    ans = input("Add another assignment? (yes/no): ").lower()
    if ans != "yes":
        break


# PROCESS RESULTS
total_FA = 0
total_SA = 0
total_weight_FA = 0
total_weight_SA = 0

# Calculate totals
for item in arr:
    weighted = (item["grade"] / 100) * item["weight"]

    if item["category"] == "FA":
        total_FA += weighted
        total_weight_FA += item["weight"]
    else:
        total_SA += weighted
        total_weight_SA += item["weight"]

#main calculations both sa and fa to find gpa
total_grade = total_FA + total_SA
total_weight = total_weight_FA + total_weight_SA
final_grade = (total_grade / total_weight) * 100
gpa = (final_grade / 100) * 5

# Determine pass/fail by checking of the students has atleast half the >
if total_FA >= (total_weight_FA / 2) and total_SA >= (total_weight_SA / 2):
    promoted = "Pass"
else:
    promoted = "Fail"


# ------------ OUTPUT RESULTS -------------
print("--------- RESULTS ------------")
print(f"Total Formative: {total_FA:.2f} / {total_weight_FA}")
print(f"Total Summative: {total_SA:.2f} / {total_weight_SA}")
print("------------------------------")
print(f"Final Grade: {final_grade:.2f} / 100")
print(f"GPA: {gpa:.2f} / 5")
print(f"Status: {promoted}")


# Identify assignments to redo
redo = []

for a in arr:
    if a["grade"] < 50:
        redo.append(a)
if redo:
    #print("Assignments to redo:")
    for r in redo:
        print(f"Resubmission: {r['name']} ")
else:
    print("No resubmission needed.")

#--save to csv

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Assignment", "Category", "Grade", "Weight"])

    for a in arr:
        writer.writerow([a["name"], a["category"], a["grade"], a["weight"]])
