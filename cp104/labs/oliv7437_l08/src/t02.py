"""
-------------------------------------------------------
Lab 8, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
# Imports
from functions import get_month_name

month_num = int(input("Enter month number: "))

name = get_month_name(month_num)

print(f"Month: {name}")
