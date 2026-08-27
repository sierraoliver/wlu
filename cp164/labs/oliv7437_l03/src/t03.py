"""
-------------------------------------------------------
Lab 3, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test

q = Queue()
q2 = Queue()

values = [20, 11]
values2 = [20, 11]
target = []

array_to_queue(q2, values2)
queue_to_array(q2, target)

print(f"Queue to Array: {target}")

array_to_queue(q, values)
print(f"Array to Queue")
length = len(q)
for x in range(length):
    data = q._values[x]
    print(data)

values = [20, 11]
print(f"Queue Test")
queue_test(values)
