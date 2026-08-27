"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-24"
-------------------------------------------------------
"""
# Imports
from functions import day_name

day_number = int(input("Enter number of the day of the week: "))

day = day_name(day_number)

print(f"Day of the Week: {day}")
