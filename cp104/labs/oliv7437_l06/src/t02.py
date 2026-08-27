"""
-------------------------------------------------------
Lab 6, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# imports
from functions import sum_odd

number = int(input("Enter a number: "))

total = sum_odd(number)

print(f"The sum of all odd numbers from 1 to {number} is {total}")
