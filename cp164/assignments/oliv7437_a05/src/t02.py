"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
from Food_utilities import read_foods
from Food import Food
from copy import deepcopy

file = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file)

source1 = Sorted_List()
source2 = Sorted_List()
source3 = Sorted_List()


foods1 = foods[0:3]
foods2 = foods[0:4]
foods3 = foods[0:6]
"""
foods1 = []
foods2 = []
foods3 = []
"""

food = foods[0:1]

for x in range(len(foods1)):
    source1.insert(foods1[x])

for x in range(len(foods3)):
    source3.insert(foods3[x])

source5 = deepcopy(source3)

# testing find
key_food = Food("Lasagna", 7, None, None)
value = source1.find(key_food)
print(f"""Key Food: 
{value}""")


# testing __eq__
equals = source1 == foods2
print(f"Equals: {equals}")

for x in range(len(foods2)):
    source2.insert(foods2[x])

# testing __getitem__
index = 0
if index < len(source3._values):
    value = source3._values[index]
    print(f"""Value at {index}:\n{value}""")


# testing __contains__
key = food[0]
b = key in source3
print(f"Testing __contains__")
print(f"contains key: {b}")

# source3.insert(food[0])

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

# testing count
number = source3.count(key)
print(f"Count of key: {number}")

# source3.insert(key)
# testing min
min_num = source3.min()
print(f"Min:\n{min_num}")

# testing max
max_num = source3.max()
print(f"Max:\n{max_num}")

# testing peek
peek = source3.peek()
print(f"Peek:\n{peek}")

# testing remove
remove = source3.remove(key)
print(f"Remove:\n{remove}")

# testing remove_many
source3.remove_many(food[0])
print(f"""Removing:
{food[0]}""")

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

source3.remove(key)
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

# testing split_key
key = source5._values[2]
#key = food[0]
target5, target6 = source5.split_key(key)
print(f"Testing split_key")
print(f"""Key:
{key}""")
print(f"Target5")
for x in range(len(target5._values)):
    data = target5._values[x]
    print(data)

print(f'Target6')
for x in range(len(target6._values)):
    data = target6._values[x]
    print(data)

# testing combine
source3.combine(target3, target4)
print(f"Testing combine")
for x in range(len(source3._values)):
    data = source3._values[x]
    print(data)

source3.insert(key)
# testing clean
source3.clean()
print(f"Testing clean")
for x in range(len(source3._values)):
    data = source3._values[x]
    print(data)

file.close()
