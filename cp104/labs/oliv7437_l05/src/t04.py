"""
-------------------------------------------------------
Lab 5, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# imports
from functions import closest

target = float(input("Enter target value: "))
v1 = float(input("Enter value one: "))
v2 = float(input("Enter value two: "))

result = closest(target, v1, v2)

print(f"The closer value to {target} is {result}")
