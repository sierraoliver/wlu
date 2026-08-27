"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

s = Priority_Queue()
s2 = Priority_Queue()
empty = Priority_Queue()

values = [11, 22, 33, 44, 55]
numbers = [66]

for x in range(len(values)):
    s.insert(values[x])

for x in range(len(numbers)):
    s2.insert(numbers[x])

# test for append_queue

print(f"Source1: {values}")
print(f"Source2: {numbers}")
print(f"Source1_append_queue(Source2)")
s._append_queue(s2)

for x in range(s._count):
    remove = s.remove()
    print(remove)


# test for insert, peek, remove, is_empty
"""
print(f"Values: {numbers}")
empty = s2.is_empty()
print(f"Empty: {empty}")

for x in range(s2._count):
    peek = s2.peek()
    print(f"Peek: {peek}")
    remove = s2.remove()
    print(f"Removed: {remove}")

empty = s2.is_empty()
print(f"Empty: {empty}")
"""

# test for split_key
"""
print(f"Source: {values}")
print(f"Split source with 90")
target1, target2 = s.split_key(90)

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

# test for split_alt
"""
print(f"Source: {numbers}")
print(f"Split Alt with source")
target1, target2 = s2.split_alt()

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

# test for combine
"""
print(f"Source1: {values}")
print(f"Source2: {numbers}")
empty.combine(s, s2)

print(f"Combine: Source1 & Source2")
for x in range(empty._count):
    remove = empty.remove()
    print(remove)
"""

# test for move_front_to_rear
"""
print(f"Source1: {values}")
print(f"Source2: {numbers}")
print(f"Source1_move_front_to_rear(Source2)")
s._move_front_to_rear(s2)

current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
"""
