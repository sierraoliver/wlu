"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import average_calories, read_foods

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)
foods = foods[0:3]

length = len(foods)
print(f"Food Calories:")
for x in range(length):
    food = foods[x]
    print(food.calories)

average = average_calories(foods)

print(f"Average Calories: {average:.2f}")

file.close()
