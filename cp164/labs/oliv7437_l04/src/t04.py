"""
-------------------------------------------------------
Lab 4, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list
from random import randint

source = List()

values = [45, 90, 1000, 2]

array_to_list(source, values)

max_num = source.max()
print(f"Max: {max_num}")

min_num = source.min()
print(f"Min: {min_num}")

value = source.peek()
contains = source.__contains__(value)
print(f"Contains {value}: {contains}")

index = randint(0, (len(source._values)-1))
value = source._values[index]
i = source.index(value)
print(f"Index of {value}: {i}")

index = randint(0, (len(source._values)-1))
value = source._values[index]
data = source.find(value)
print(f"Find {value}: {data}")
