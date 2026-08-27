"""
-------------------------------------------------------
Lab 2, Task 7
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-09-10"
-------------------------------------------------------
"""
# Imports

# Constants

flyers = int(input("Number of flyers: "))

volunteers = int(input("Number of volunteers: "))

per_person = flyers // volunteers

left_over = flyers % volunteers

print("Flyers per volunteer: ", per_person)

print("Flyers left over: ", left_over)
