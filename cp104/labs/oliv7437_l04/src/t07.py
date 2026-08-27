"""
-------------------------------------------------------
Lab 4, Task 7
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import total_change

nickels = int(input("Number of Nickels: "))
dimes = int(input("Number of Dimes: "))
quarters = int(input("Number of Quarters: "))
loonies = int(input("Number of Loonies: "))
toonies = int(input("Number of Toonies: "))

total = total_change(nickels, dimes, quarters, loonies, toonies)

print(f"Total Change: ${total:.2f}")
