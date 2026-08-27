"""
-------------------------------------------------------
Assignment 4, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import colour_combine

first_colour = input("Enter first primary colour: ")

second_colour = input("Enter second primary colour: ")

secondary_colour = colour_combine(first_colour, second_colour)

print(f"Those 2 colours combined create: {secondary_colour}")
