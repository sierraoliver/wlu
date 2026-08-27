"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_search, read_foods

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)

origin = int(input("Origin: "))
max_cals = int(input("Max Calories: "))
veg = input("Vegetarian (Y/N): ")

if veg == "Y":
    is_veg = True

elif veg == "N":
    is_veg = False

result = food_search(foods, origin, max_cals, is_veg)

print()

length = len(result)
for x in range(length):
    food = result[x]
    print(food.__str__())

file.close()
