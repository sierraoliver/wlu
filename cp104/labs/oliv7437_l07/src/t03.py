"""
-------------------------------------------------------
Lab 7, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-02"
-------------------------------------------------------
"""
# Imports
from functions import population_growth

target_pop = int(input("Target Population: "))
current_pop = int(input("Current Population: "))
rate = float(input("Percent Rate Growth: "))

years = population_growth(target_pop, current_pop, rate)

print(f"Year to Reach {target_pop} is {years}")
