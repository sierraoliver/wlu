"""
-------------------------------------------------------
Lab 6, Task 11
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-22"
-------------------------------------------------------
"""
# Imports
from functions import retirement

age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
increase = float(input("Enter increase in salary per year: "))

retirement(age, salary, increase)
