"""
-------------------------------------------------------
Assignment 9, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import student_stats

students = open("students.txt", "r", encoding="utf-8")

lowest, highest, average = student_stats(students)

print(f"{lowest}, {highest}, {average}")

students.close()
