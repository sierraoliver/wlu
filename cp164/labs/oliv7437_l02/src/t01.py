"""
-------------------------------------------------------
Lab 2, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-16"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

numbers = [1, 2, 3, 4, 5]
print(numbers)
s = Stack()

for x in range(len(numbers)):
    num = numbers[x]
    s.push(num)

result = s.is_empty()
print(f"Is Empty: {result}")

value = s.peek()
print(f"Peek: {value}")

add = 22
s.push(add)
added = s.peek()
print(f"""Push {add}, Peek: {added}""")

removed = s.pop()
top = s.peek()
print(f"""Remove:{removed}, Peek: {top}""")
