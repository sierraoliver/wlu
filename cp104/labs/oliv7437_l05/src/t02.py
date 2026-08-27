"""
-------------------------------------------------------
Lab 5, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
from functions import get_weight

mass = float(input("Mass of object (kg): "))

weight, message = get_weight(mass)

print(f"The weight of object is {weight:.1f} and the weight is {message}")
