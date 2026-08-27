"""
-------------------------------------------------------
Lab 9, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from functions import hash_table

file = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file)

slots = 7

hash_table(slots, foods)

file.close()
