"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import calories_by_origin, read_foods

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)

origin = int(input("Origin: "))

average = calories_by_origin(foods, origin)

print(f"Average: {average:.2f}")

file.close()
