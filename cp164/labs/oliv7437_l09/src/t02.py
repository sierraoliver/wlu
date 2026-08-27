"""
-------------------------------------------------------
Lab 9, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

s = Hash_Set(7)

values = [1, 2, 3, 4]

print(f"Insert: {values}")

for x in range(len(values)):
    s.insert(values[x])

print(f"Hash Table")
for x in range(len(s._table)):
    for y in range(len(s._table[x]._values)):
        value = s._table[x]._values[y]
        print(value)

print(f"Remove: 1")
s.remove(1)

print(f"Resulting Table")
for x in range(len(s._table)):
    for y in range(len(s._table[x]._values)):
        value = s._table[x]._values[y]
        print(value)
