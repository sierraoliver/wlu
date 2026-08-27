"""
-------------------------------------------------------
Lab 9, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports
from functions import url_categorize

url = input("Enter url: ")

url_type = url_categorize(url)

print(f"{url_type}")
