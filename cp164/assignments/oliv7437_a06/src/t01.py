"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

s = Queue()
empty = Queue()
source1 = Queue()
source2 = Queue()

data = [11]
numbers = []
values = [11]

for x in range(len(values)):
    source1.insert(values[x])

for x in range(len(numbers)):
    source2.insert(numbers[x])

for x in range(len(data)):
    s.insert(data[x])

# test for move_front_to_rear
"""
print(f"Source1: {data}")
print(f"Source2: {values}")
print(f"Source1_move_front_to_rear(Source2)")
s._move_front_to_rear(source1)

for x in range(s._count):
    remove = s.remove()
    print(remove)
"""

# test for append_queue
"""
print(f"Source1: {data}")
print(f"Source2: {values}")
print(f"Source1_append_queue(Source2)")
s._append_queue(source1)

for x in range(s._count):
    remove = s.remove()
    print(remove)
"""

# test for combine
"""
print(f"Source1: {values}")
print(f"Source2: {numbers}")
empty.combine(source1, source2)

print(f"Combine: Source1 & Source2")
for x in range(empty._count):
    remove = empty.remove()
    print(remove)
"""

# test for empty, insert, remove, peek
"""
print(f"Values: {data}")
empty = s.is_empty()
print(f"Empty: {empty}")

for x in range(s._count):
    peek = s.peek()
    print(f"Peek: {peek}")
    remove = s.remove()
    print(f"Removed: {remove}")

empty = s.is_empty()
print(f"Empty: {empty}")
"""

# test for eq and split_alt

print(f"Source1: {values}")
print(f"Source2: {data}")

equals = s == source1
print(f"Equals: {equals}")
"""
print(f"Split Alt with source2")
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
