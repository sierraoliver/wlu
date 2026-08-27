"""
-------------------------------------------------------
Lab 9, Task 10
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports
from functions import text_analyze

text = input("Enter text: ")

upper, lower, digits, space = text_analyze(text)

print(f"{upper}, {lower}, {digits}, {space}")
