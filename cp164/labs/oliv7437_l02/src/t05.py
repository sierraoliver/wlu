"""
-------------------------------------------------------
Lab 2, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import stack_test

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)

foods = foods[0:1]

stack_test(foods)

file.close()
