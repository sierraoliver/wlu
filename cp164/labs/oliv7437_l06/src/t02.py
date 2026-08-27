"""
-------------------------------------------------------
Lab 6, Task 2
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

values = [22, 11, 33]
print(f"Values: {values}")

for x in range(len(values)):
    s.prepend(values[x])

previous, current, index = s._linear_search(11)

print(f"""Previous: {previous._value}
Current: {current._value}
Index: {index}""")
