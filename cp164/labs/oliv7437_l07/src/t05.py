"""
-------------------------------------------------------
Lab 7, Task 5
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
source1 = List()
source2 = List()

numbers = [22, 33, 11, 55, 44]
values = [22, 33, 66, 55, ]

print(f"Source 1: {numbers}")
print(f"Source 2: {values}")

for x in range(len(numbers)):
    source1.append(numbers[x])

for x in range(len(values)):
    source2.append(values[x])

s.union_r(source1, source2)

print(f"Union:")
current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
