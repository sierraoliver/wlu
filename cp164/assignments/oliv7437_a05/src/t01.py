"""
-------------------------------------------------------
Assignment 5, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list
from Food_utilities import read_foods
from copy import deepcopy

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)


foods1 = deepcopy(foods[:2])
foods2 = deepcopy(foods[:2])
foods3 = deepcopy(foods[:6])

"""
foods1 = []
foods2 = []
foods3 = []
"""

source1 = List()
source2 = List()
source3 = List()

array_to_list(source1, foods1)
array_to_list(source3, foods3)

# testing __eq__
equals = source1 == foods2
print(f"Equals: {equals}")

array_to_list(source2, foods2)

# testing __getitem__
index = 0
if index < len(source3._values):
    value = source3._values[index]
    print(f"""Value at {index}:\n{value}""")

# testing append
#item = source1._values[0]
item = foods[0]
source3.append(item)
print(f"""Appended:
{item}
Got:
{source3._values[len(source3)-1]}""")

# testing remove_front
front = source3.remove_front()
if source3.is_empty():
    new_front = []
else:
    new_front = source3.peek()
print(f"""Front Before:
{front}
Front After:
{new_front}""")

# testing remove_many
source3.remove_many(item)
print(f"""Removing:
{item}""")

print(f"Check source3:")
for x in range(len(source3._values)):
    data = source3._values[x]
    print(data)

# testing union
source3.union(source1, source2)
print(f"Union test of source3:")
for y in range(len(source3._values)):
    data = source3._values[y]
    print(data)

# testing prepend
source3.prepend(item)
print(f"""Prepend:
{item}
Found:
{source3.peek()}""")

source3.remove_front()

# testing intersection
source3.intersection(source1, source2)
print(f"Testing intersection on source3")
for z in range(len(source3._values)):
    data = source3._values[z]
    print(data)

# testing split
source4 = deepcopy(source3)
length = len(source4._values)
target1, target2 = source4.split()
print(f"Testing split - length of source = {length}")
print(f'Target1')
for x in range(len(target1._values)):
    data = target1._values[x]
    print(data)
print(f'Target2')
for x in range(len(target2._values)):
    data = target2._values[x]
    print(data)

# testing split_alt
target3, target4 = source3.split_alt()
print(f"Testing split_alt")
print(f'Target3')
for x in range(len(target3._values)):
    data = target3._values[x]
    print(data)
print(f'Target4')
for x in range(len(target4._values)):
    data = target4._values[x]
    print(data)

# testing combine
source3.combine(target3, target4)
print(f"Testing combine")
for x in range(len(source3._values)):
    data = source3._values[x]
    print(data)

# testing clean
source3.clean()
print(f"Testing clean")
for x in range(len(source3._values)):
    data = source3._values[x]
    print(data)


file.close()
