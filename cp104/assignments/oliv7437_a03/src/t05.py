"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import falling_distance

time = int(input("Enter the time the object has been falling: "))

distance = falling_distance(time)

print(f"Distance the object has fallen is {distance}")
