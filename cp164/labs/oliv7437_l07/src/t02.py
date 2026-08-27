"""
-------------------------------------------------------
Lab 7, Task 2
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

numbers = [22, 33, 11, 55, 44]
values = [22, 33, 11, 55, 44]

print(f"Source 1: {numbers}")
print(f"Source 2: {values}")

for x in range(len(numbers)):
    s.append(numbers[x])

for x in range(len(values)):
    source1.append(values[x])

identical = s.is_identical_r(source1)
print(f"Identical: {identical}")
