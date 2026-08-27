"""
-------------------------------------------------------
Assignment 8, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports
from morse import ByCode

data = (('A', '.-'), ('B', '-...'), ('C', '-.-.'))

version1 = data[1]
value1 = ByCode(version1[0], version1[1])

version2 = data[0]
value2 = ByCode(version2[0], version2[1])

# testing eq
print(f"testing eq")
print(f"Value 1: {version1}")
print(f"Value 2: {version2}")
result = value1 == value2
print(f"Equals: {result}")

print()

# testing le
print(f"testing le")
print(f"Value 1: {version1}")
print(f"Value 2: {version2}")
result = value1 <= value2
print(f"Result: {result}")

print()

# tesing lt
print(f"testing lt")
print(f"Value 1: {version1}")
print(f"Value 2: {version2}")
result = value1 < value2
print(f"Result: {result}")
