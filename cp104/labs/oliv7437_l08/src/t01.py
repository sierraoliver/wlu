"""
-------------------------------------------------------
Lab 8, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
# Imports
from functions import get_weekday_name

weekday = int(input("Enter number for the day of the week: "))

name = get_weekday_name(weekday)

print(f"Day of the Week: {name}")
