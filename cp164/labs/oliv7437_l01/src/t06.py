"""
-------------------------------------------------------
Lab 1, Task 6
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from Food_utilities import write_foods
from Food_utilities import read_foods

r_file = open("foods.txt", "r", encoding="utf-8")
w_file = open("new_foods.txt", "w+", encoding="utf-8")

foods = read_foods(r_file)

write_foods(w_file, foods)

r_file.close()
w_file.close()
