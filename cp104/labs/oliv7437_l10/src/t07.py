"""
-------------------------------------------------------
Lab 10, Task 7
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-22"
-------------------------------------------------------
"""
# Imports
from functions import append_max_num

numbers_file = open("numbers.txt", "r+", encoding="utf-8")

number = append_max_num(numbers_file)

print(f"{number} is appended to numbers.txt")

numbers_file.close()
