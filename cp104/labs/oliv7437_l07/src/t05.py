"""
-------------------------------------------------------
Lab 7, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-02"
-------------------------------------------------------
"""
# Imports
from functions import positive_statistics

minimum, maximum, total, average = positive_statistics()

print(f"""
Minimum: {minimum:.2f}
Maximum: {maximum:.2f}
Total: {total:.2f}
Average: {average:.2f}
""")
