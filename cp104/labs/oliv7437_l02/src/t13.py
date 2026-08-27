"""
-------------------------------------------------------
Lab 2, Task 13
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-09-10"
-------------------------------------------------------
"""
# Imports

# Constants
MIDTERM = 0.35
EXAM = 0.65


midterm_mark = float(input("Midterm mark (%): "))

exam_mark = float(input("Exam mark (%): "))

final_grade = (midterm_mark * MIDTERM) + (exam_mark * EXAM)

print(f"Final grade (%):  {final_grade:.1f}")
