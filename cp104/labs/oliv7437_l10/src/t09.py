"""
-------------------------------------------------------
Lab 10, Task 9
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_value

numbers_file = open("numbers.txt", "r", encoding="utf-8")

value = int(input("Value to count: "))

count = count_frequency_value(numbers_file, value)

print(f"{value} appears {count} time(s)")

numbers_file.close()
