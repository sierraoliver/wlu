"""
-------------------------------------------------------
Lab 6, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
# Imports
from List_linked import List

s = List()

numbers = [22, 33, 11, 55, 44]

for x in range(len(numbers)):
    s.insert(2, numbers[x])

current = s._front
for x in range(len(numbers)):
    print(current._value)
    current = current._next

s.prepend(90)
peek = s.peek()
print(f"Prepend")
print(s._front._value)

s.append(40)
print(f"Append")
print(s._rear._value)
