"""
-------------------------------------------------------
Lab 4, Task 10
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import population

size = int(input("Current Population: "))
births = int(input("Average Seconds Between Births: "))
deaths = int(input("Average Seconds Between Deaths: "))
immigrants = int(input("Average Seconds Between Immigrations: "))
years = int(input("Years to Calculate New Population: "))

new_size = population(size, births, deaths, immigrants, years)

print(f"The future population is {new_size}")
