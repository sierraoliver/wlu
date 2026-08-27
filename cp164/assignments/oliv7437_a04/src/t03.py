"""
-------------------------------------------------------
Assignment 4 ,Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue
from functions import queue_split_alt

source = Queue()

nums = [1]
print(f"Source: {nums}")

array_to_queue(source, nums)

target1, target2 = queue_split_alt(source)

print(f"Target 1")
for x in range(len(target1._values)):
    print(target1._values[x])

print(f"Target 2")
for x in range(len(target2._values)):
    print(target2._values[x])
