"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

source = Queue()
target = Queue()
source_list = []
target_list = []
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# testing empty
if source.is_empty():
    print(f"Source is empty")

else:
    print(f"Source is not empty")

# testing insert function
for x in range(len(num1)):
    num = num1[x]
    source.insert(num)

for y in range(len(num2)):
    value = num2[y]
    target.insert(value)

# testing full
if source.is_full():
    print(f"Source is full")

else:
    print(f"Source is not full")

# testing length
n = len(source)
print(f"Length of source: {n}")

# remove values
remove_value = 0
for r in range(remove_value):
    target.remove()

# printing queues
for z in range(len(source._values)):
    source_list.append(source._values[z])
    target_list.append(target._values[z])

print(f"Source Queue: {source_list}")
print(f"Target Queue: {target_list}")

# testing equal function
equals = source == target
print(f"Equal: {equals}")

# testing peek and remove
while not source.is_empty():
    peek = source.peek()
    remove = source.remove()

    print(f"Peek: {peek}")
    print(f"Removed: {remove}")

# making sure it is empty
empty = source.is_empty()
print(f"Empty expects: True")
print(f"Empty got: {empty}")
