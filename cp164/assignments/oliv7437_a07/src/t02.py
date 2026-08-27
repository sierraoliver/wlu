"""
-------------------------------------------------------
Assignment 7, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List

s = Sorted_List()
source = Sorted_List()
source2 = Sorted_List()

values = []
numbers = [1, 2, 3]
datas = [4, 5, 6]

for value in values:
    s.insert(value)

for number in numbers:
    source.insert(number)

for data in datas:
    source2.insert(data)

# testing contains
"""
print(f"Values: {values}")
value = 0
b = value in s
print(f"Contains {value}: {b}")
"""

# testing eq
"""
equals = s == source
print(f"Source1: {values}")
print(f"Source2: {numbers}")
print(f"Equals: {equals}")
"""

# testing getitem
"""
print(f"Values: {values}")
index = 0
value = s[index]
print(f"Value at {index}: {value}")
"""

# testing clean
"""
print(f"Values: {values}")
print(f"--clean--")
s.clean()

current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
"""

# testing count
"""
print(f"Values: {values}")
num = 5
n = s.count(num)
print(f"Count of {num}: {n}")
"""

# testing find
"""
print(f"Values: {values}")
num = 11
value = s.find(num)
print(f"Find {num}: {value}")
"""

# testing index
"""
print(f"Values: {values}")
num = 11
index = s.index(num)
print(f"Index of {num}: {index}")
"""


# testing intersection
"""
print(f"Intersection")
print(f"Source1: {numbers}")
print(f"Source2: {datas}")
s.intersection(source, source2)
current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
"""

# testing max
"""
print(f"Values: {values}")
num = s.max()
print(f"Max: {num}")
"""

# testing min
"""
print(f"Values: {values}")
num = s.min()
print(f"Min: {num}")
"""

# testing peek
"""
print(f"Values: {values}")
print(f"Peek: {s.peek()}")
"""

# testing remove
"""
print(f"Values: {values}")
num = 5
print(f"--remove {num}--")
s.remove(num)
current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
"""

# testing remove_front
"""
print(f"Values: {values}")
print(f"--removefront--")
s.remove_front()
current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
"""

# testing union

print(f"Union")
print(f"Source1: {numbers}")
print(f"Source2: {datas}")
s.union(source, source2)
current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
