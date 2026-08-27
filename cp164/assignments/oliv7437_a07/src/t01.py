"""
-------------------------------------------------------
Assignment 7, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from List_linked import List

s = List()
source = List()
source2 = List()

values = []
numbers = [1, 2, 3]
datas = [4, 5, 6]

for value in values:
    s.append(value)

for number in numbers:
    source.append(number)

for data in datas:
    source2.append(data)

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
index = -2
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

# testing combine
"""
print(f"Combine")
print(f"Source1: {numbers}")
print(f"Source2: {datas}")
s.combine(source, source2)
current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
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

# testing prepend
"""
print(f"Values: {values}")
num = 0
print(f"Prepend: {num}")
s.prepend(num)
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

# testing remove_many
"""
print(f"Values: {values}")
value = 11
print(f"--removemany {value}--")
s.remove_many(value)
current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
"""

# testing split
"""
print(f"Values: {values}")
print(f"--split--")
target1, target2 = s.split()
print(f"Target1")
current = target1._front
for x in range(target1._count):
    print(current._value)
    current = current._next
print(f"Target2")
current = target2._front
for x in range(target2._count):
    print(current._value)
    current = current._next
"""

# testing split_alt
"""
print(f"Values: {values}")
print(f"--splitalt--")
target1, target2 = s.split_alt()
print(f"Target1")
current = target1._front
for x in range(target1._count):
    print(current._value)
    current = current._next
print(f"Target2")
current = target2._front
for x in range(target2._count):
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
