"""
-------------------------------------------------------
Lab 5, Task 9
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports
from functions import wind_speed

speed = int(input("Enter wind speed (km/hr): "))

category = wind_speed(speed)

print(f"That wind speed is: {category}")
