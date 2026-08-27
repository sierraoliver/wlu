"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import extract_date

date_number = int(input("Enter the date (YYYYMMDD): "))

year, month, day = extract_date(date_number)

print(f"Reformatted date: {year:02d}/{month:02d}/{day:02}")
