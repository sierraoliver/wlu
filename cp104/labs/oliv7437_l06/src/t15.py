"""
-------------------------------------------------------
Lab 6, Task 15
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-27"
-------------------------------------------------------
"""
# Imports
from functions import statistics

number_of_values = int(input("Enter number of values: "))

minimum, maximum, total, average = statistics(number_of_values)

print(f"""
Minimum value: {minimum:.2f}
Maximum value: {maximum:.2f}
Total: {total:.2f}
Average: {average:.2f}
""")
