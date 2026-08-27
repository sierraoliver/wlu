"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_table, read_foods

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)

food_table(foods)

file.close()
