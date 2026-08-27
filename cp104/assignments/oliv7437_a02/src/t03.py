"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""

date = int(input("Enter a date in the format YYYMMDD: "))

# calculations
year = date // 10000
month = (date//100) % 100
day = date % 100

print()

print(f"The reformatted date: {year}/{month:02d}/{day:02d}")
