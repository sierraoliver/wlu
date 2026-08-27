"""
-------------------------------------------------------
Lab 7, Task 3
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

print(f"Source: {numbers}")

for x in range(len(numbers)):
    s.append(numbers[x])

target1, target2 = s.split_alt_r()

print(f"Split_Alt:\n")

print(f"Target1:")
current = target1._front
for x in range(target1._count):
    print(current._value)
    current = current._next

print(f"Target2:")
current = target2._front
for x in range(target2._count):
    print(current._value)
    current = current._next
