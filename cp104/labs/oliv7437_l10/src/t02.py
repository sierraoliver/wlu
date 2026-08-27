"""
-------------------------------------------------------
Lab 10, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-22"
-------------------------------------------------------
"""
# Imports
from functions import customer_by_id

customer_file = open("customers.txt", "r", encoding="utf-8")

id_number = input("Enter an ID: ")

result = customer_by_id(customer_file, id_number)

print(f"{result}")

customer_file.close()
