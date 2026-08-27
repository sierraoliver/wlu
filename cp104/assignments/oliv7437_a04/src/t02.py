"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import pollution_ranking

air_quality = int(input("Enter the AQI: "))

pollution = pollution_ranking(air_quality)

print(f"The pollution level is: {pollution}")
