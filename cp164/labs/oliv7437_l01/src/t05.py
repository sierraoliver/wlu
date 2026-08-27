"""
-------------------------------------------------------
Lab 1, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)

length = len(foods)

for x in range(length):
    food = foods[x]
    food.__str__()
    print(food)

file.close()
