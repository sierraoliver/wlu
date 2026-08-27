"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year

year = int(input("Enter year: "))

leap_year = is_leap_year(year)

print(f"Leap Year: {leap_year}")
