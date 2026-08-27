"""
-------------------------------------------------------
Assignment 10, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-29"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Values: {values}")

s = Deque()

for x in range(len(values)):
    s.insert_rear(values[x])

Sorts.gnome_sort(s)

data = []
current = s._front
for x in range(s._count):
    data.append(current._value)
    current = current._next

print(f"Gnome Sort: {data}")
