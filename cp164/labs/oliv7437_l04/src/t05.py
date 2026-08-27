"""
-------------------------------------------------------
Lab 4, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from List_array import List

source = List()
numbers = [22, 33, 11, 55, 44]
print(f"Array: {numbers}")

for x in range(len(numbers)):
    number = numbers[x]
    source.append(number)

print(f"source[-4] = 4")
source[-4] = 4

for y in range(len(source._values)):
    data = source._values[y]
    print(data)

value = source[-4]
print(f"Value at source[-4]: {value}")
