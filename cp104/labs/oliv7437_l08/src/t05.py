"""
-------------------------------------------------------
Lab 8, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
# Imports
from functions import get_lotto_numbers

lotto_num = int(input("Number of lotto numbers: "))
low = int(input("Low value of lottery number range: "))
high = int(input("High value of lottery number range: "))

numbers = get_lotto_numbers(lotto_num, low, high)

print(f"{numbers}")
