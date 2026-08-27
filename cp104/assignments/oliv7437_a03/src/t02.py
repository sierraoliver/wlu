"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports
from functions import lawn_mow_time

width = float(input("Enter the width of lawn (m): "))
length = float(input("Enter the length of lawn (m): "))
speed = float(input("Square meters cut per minute: "))

time = lawn_mow_time(width, length, speed)

print(f"Time required to mow the lawn is {time:.1f}")
