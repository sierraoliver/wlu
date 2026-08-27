"""
-------------------------------------------------------
Assignment 9, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import read_integers

numbers = open("numbers.txt", "r", encoding="utf-8")

number_list = read_integers(numbers)

print(f"{number_list}")

numbers.close()
