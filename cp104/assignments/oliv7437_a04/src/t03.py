"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import largest_average

value_one = float(input("Enter a number: "))
value_two = float(input("Enter another number: "))
value_three = float(input("Enter another number: "))

average = largest_average(value_one, value_two, value_three)

print(f"The average of the 2 largest numbers is: {average:.1f}")
