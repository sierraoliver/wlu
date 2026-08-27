"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import by_origin, read_foods

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)

origin = int(input(f"Origin: "))

origins = by_origin(foods, origin)

length = len(origins)
for x in range(length):
    origin = origins[x]
    print(origin.__str__())

file.close()
