"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-29"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts
from List_linked import List

a = List()
values = [22, 33, 11, 0, 5, 87, 100]

for x in range(len(values)):
    a.append(values[x])

print(f"Values: {values}")

Sorts.radix_sort(a)

data = []

current = a._front
for x in range(a._count):
    data.append(current._value)
    current = current._next

print(f"Radix Sort: {data}")
