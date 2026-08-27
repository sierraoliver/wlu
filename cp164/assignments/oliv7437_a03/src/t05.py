"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack

string = input(f"Palindrome: ")

palindrome = is_palindrome_stack(string)

if palindrome:
    print(f"It is a palindrome")

else:
    print(f"It is not a palindrome")
