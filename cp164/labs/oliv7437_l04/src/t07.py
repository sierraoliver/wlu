"""
-------------------------------------------------------
Lab 4, Task 7
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from utilities import list_test
from Food_utilities import read_foods

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)
foods = foods[0:2]

list_test(foods)

file.close()
