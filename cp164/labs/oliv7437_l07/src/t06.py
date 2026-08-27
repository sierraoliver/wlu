"""
-------------------------------------------------------
Lab 7, Task 6
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

s = List()

numbers = [22, 33, 11, 55, 44]

print(f"Original List: {numbers}")

for x in range(len(numbers)):
    s.append(numbers[x])

s.reverse_r()

print(f"Reversed List: ")
current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
