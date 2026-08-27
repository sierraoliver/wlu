"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from functions import calories_treadmill

per_min = float(input("Enter the number of calories burned per min: "))

minutes = int(input("Enter total minutes: "))

calories_treadmill(per_min, minutes)
