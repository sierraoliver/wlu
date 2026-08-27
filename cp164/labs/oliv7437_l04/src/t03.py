"""
-------------------------------------------------------
Lab 4, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list
from random import randint

source = List()

values = [1, 2, 3]
print(f"Array: {values}")

array_to_list(source, values)

num = int(input(f"Append: "))
source.append(num)
print(f"Appended: {source._values[(len(source._values)-1)]}")

insert_num = int(input(f"Insert: "))
index = randint(0, (len(source._values)-1))
print(f"Index: {index}")
source.insert(index, insert_num)
print(f"Inserted Number: {source._values[index]}")

random_num = randint(0, (len(source._values)-1))
key = source._values[random_num]
remove = source.remove(key)
print(f"Removed: {remove}")

for x in range(len(source._values)):
    data = source._values[x]
    print(data)
