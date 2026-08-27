"""
-------------------------------------------------------
Lab 3, Task 6
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import pq_to_array, priority_queue_test, array_to_pq
from Food_utilities import read_foods
from copy import deepcopy

file = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file)
foods = foods[0:2]
foods2 = deepcopy(foods)

pq = Priority_Queue()
pq2 = Priority_Queue()

array_to_pq(pq, foods)

print(f"Array to PQ")
length = pq.__len__()
for x in range(length):
    data = pq._values[x]
    print(data)


print(f"PQ Test")
priority_queue_test(foods2)
print()

target = []
pq_to_array(pq, target)
print(f"PQ to Array")
leng = len(target)
for y in range(leng):
    value = target[y]
    print(value)

file.close()
