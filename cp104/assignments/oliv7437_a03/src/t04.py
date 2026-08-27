"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import multiply_fractions

num1 = int(input("Enter numerator 1: "))
den1 = int(input("Enter denominator 1: "))

num2 = int(input("Enter numerator 2: "))
den2 = int(input("Enter denominator 2: "))

num, den, product = multiply_fractions(num1, den1, num2, den2)

print(f"Numerator: {num}, Denominator: {den}, Product: {product}")
