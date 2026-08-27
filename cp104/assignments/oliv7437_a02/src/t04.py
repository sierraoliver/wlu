"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-02"
-------------------------------------------------------
"""
flyers = int(input("Number of flyers: "))
people = int(input("Number of delivery people: "))

flyers_per_person = flyers//people
leftover_flyers = flyers % people

print()

print(f"Flyers per delivery person: {flyers_per_person}")
print(f"Flyers left over: {leftover_flyers}")
