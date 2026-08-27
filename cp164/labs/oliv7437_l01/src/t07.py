"""
-------------------------------------------------------
Lab 1, Task 7
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import get_vegetarian
from Food_utilities import read_foods

file = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file)

veggies = get_vegetarian(foods)

length = len(veggies)

for x in range(length):
    veg = veggies[x]

    veg.__str__()
    print(veg)

file.close()
