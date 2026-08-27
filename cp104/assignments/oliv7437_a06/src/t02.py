"""
Assignment 6, Task 
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports
from functions import detect_prime

number = int(input("Enter a number: "))

prime = detect_prime(number)

print(f"{prime}")
