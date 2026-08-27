"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque

s = Deque()
s2 = Deque()

values = []
numbers = []

for x in range(len(values)):
    s.insert_rear(values[x])

for x in range(len(numbers)):
    s2.insert_rear(numbers[x])


# test for insert, empty, peek, remove
"""
empty = s.is_empty()
print(f"Empty: {empty}")
print(f"Values: {values}")
print(f"insert_rear, peek_rear, remove_rear")
for x in range(s._count):
    peek = s.peek_rear()
    print(f"Peek: {peek}")
    remove = s.remove_rear()
    print(f"Removed: {remove}")

empty = s.is_empty()
print(f"Empty: {empty}")

print(f"Values: {numbers}")
print(f"insert_front, peek_front, remove_fornt")
for x in range(s2._count):
    peek = s2.peek_front()
    print(f"Peek: {peek}")
    remove = s2.remove_front()
    print(f"Removed: {remove}")
"""

# test eq
print(f"Source1: {values}")
print(f"Source2: {numbers}")
equals = s == s2
print(f"Equals: {equals}")

# test for swap
"""
print(f"Values: {values}")
one = s._front._next
two = one._next
s._swap(one, one)
print(f"Swap (1,1)")
current = s._front
for x in range(s._count):
    print(current._value)
    current = current._next
"""
