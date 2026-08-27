"""
-------------------------------------------------------
Lab 4, Task 14
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import time_values

seconds = int(input("Enter number of seconds: "))

days, hours, minutes = time_values(seconds)

print(
    f"There are {days} days, {hours} hours and {minutes} minutes in {seconds} seconds")
