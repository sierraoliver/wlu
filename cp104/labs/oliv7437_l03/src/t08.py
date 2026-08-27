"""
-------------------------------------------------------
Lab 3, Task 8
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-09-11"
-------------------------------------------------------
"""
# Imports

# Constants

dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

total = dirt+gravel+sand

print("Material  Cubic Meters")
print(f"Dirt     {dirt:7.1f}")
print(f"Gravel   {gravel:7.1f}")
print(f"Sand     {sand:7.1f}")
print(f"Total    {total:7.1f}")
