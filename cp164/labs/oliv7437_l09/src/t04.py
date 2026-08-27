"""
-------------------------------------------------------
Lab 9, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from Food_utilities import read_foods

file = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file)
foods = foods[:5]

s = Hash_Set(7)

for x in range(len(foods)):
    s.insert(foods[x])

print(f"---rehash---")
print()
s._rehash()

s.debug()

file.close()
