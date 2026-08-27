"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import file_top

file = open("people.txt", "r", encoding="utf-8")

lines = int(input("Number of lines to print: "))
print()

file_top(file, lines)

file.close()
