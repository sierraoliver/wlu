"""
-------------------------------------------------------
Lab 10, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-20"
-------------------------------------------------------
"""
# Imports
from test_Sorts_array import create_sorted
from test_Sorts_array import create_reversed
from test_Sorts_array import create_randoms

values = create_sorted()
print(f"Sorted:")
list = []
for x in range(len(values)):
    list.append(values[x]._value)
print(list)

values = create_reversed()
print(f"Reversed:")
list = []
for x in range(len(values)):
    list.append(values[x]._value)
print(list)

values = create_randoms()
print(f"Random:")
list = []
for x in range(len(values)):
    col = values[x]
    cols = []
    for y in range(len(col)):
        cols.append(col[y]._value)

    list.append(cols)
print(list)
