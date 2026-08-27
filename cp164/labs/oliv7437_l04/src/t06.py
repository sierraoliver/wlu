"""
-------------------------------------------------------
Lab 4, Task 6
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list, list_to_array

source = List()

numbers = [1, 2, 3, 4, 5, 6]
target = []

print(f"Original Array: {numbers}")

array_to_list(source, numbers)
print(f"Array to List")
for x in range(len(source._values)):
    data = source._values[x]
    print(data)

list_to_array(source, target)
print(f"List to Array")
print(target)
