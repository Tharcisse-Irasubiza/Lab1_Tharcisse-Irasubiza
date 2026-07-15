#!/usr/bin/env python3
import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ").strip()
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Check if file has headers and rows
            rows = list(reader)
            if not rows:
                print(f"Error: The file '{filename}' is empty.")
                sys.exit(1)
                
            for row in rows:
                # Basic check for empty or missing values
                if not row.get('assignment') or not row.get('group') or not row.get('score') or not row.get('weight'):
                    print("Error: Malformed row or missing field data in CSV.")
                    sys.exit(1)
                    
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'].strip(),
                    'group': row['group'].strip(),
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except ValueError:
        print("Error: Non-numeric values found in score or weight columns.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Evaluates grades, validates weights/scores, calculates GPA, 
    determines pass/fail standing, and evaluates resubmission options.
    """
    print("\n--- Processing Grades ---")
    
    # a) Grade Validation: Check if all scores are percentage-based (0-100)
    for row in data:
        if not (0 <= row['score'] <= 100):
            print(f"Error Validation Failed: Score for '{row['assignment']}' is {row['score']}. It must be between 0 and 100.")
            sys.exit(1)

    # b) Weight Validation: (Total=100, Summative=40, Formative=60)
    total_weight = sum(row['weight'] for row in data)
    formative_weight = sum(row['weight'] for row in data if row['group'].lower() == 'formative')
    summative_weight = sum(row['weight'] for row in data if row['group'].lower() == 'summative')

    if total_weight != 100:
        print(f"Weight Validation Error: Total weight equals {total_weight}, but it must equal exactly 100.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Weight Validation Error: Formative weight equals {formative_weight}, but it must equal exactly 60.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Weight Validation Error: Summative weight equals {summative_weight}, but it must equal exactly 40.")
        sys.exit(1)

    # c) Calculate the Final Grade and GPA
    total_grade = sum(row['score'] * (row['weight'] / 100.0) for row in data)
    gpa = (total_grade / 100.0) * 5.0

    # Calculate weighted percentage averages within each unique category
    formative_earned = sum(row['score'] * row['weight'] for row in data if row['group'].lower() == 'formative')
    formative_percentage = formative_earned / formative_weight if formative_weight > 0 else 0

    summative_earned = sum(row['score'] * row['weight'] for row in data if row['group'].lower() == 'summative')
    summative_percentage = summative_earned / summative_weight if summative_weight > 0 else 0

    print(f"Formative Average: {formative_percentage:.2f}%")
    print(f"Summative Average: {summative_percentage:.2f}%")
    print(f"Overall Final Grade: {total_grade:.2f}%")
    print(f"Calculated GPA: {gpa:.2f}")

    # d) Determine Pass/Fail status (>= 50% in BOTH categories)
    if formative_percentage >= 50 and summative_percentage >= 50:
        status = "PASSED"
    else:
        status = "FAILED"

    # e) Check for failed formative assignments (< 50%) and resubmission eligibility
    failed_formatives = [row for row in data if row['group'].lower() == 'formative' and row['score'] < 50]
    
    resubmit_assignments = []
    if failed_formatives:
        # Find the maximum weight among the failed formatives
        max_weight = max(row['weight'] for row in failed_formatives)
        # Handle ties: track all assignments sharing that maximum weight
        resubmit_assignments = [row['assignment'] for row in failed_formatives if row['weight'] == max_weight]

    # f) Print the final decision (PASSED / FAILED) and resubmission options
    print(f"\nFinal Standing: {status}")
    print("-------------------------")
    
    if status == "FAILED":
        if resubmit_assignments:
            print("Eligible Formative Assignment(s) for Resubmission (Highest Weight):")
            for assignment in resubmit_assignments:
                print(f" - {assignment}")
        else:
            print("No individual formative assignments failed, but overall criteria were not met.")
    else:
        print("Congratulations! No resubmissions required.")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
