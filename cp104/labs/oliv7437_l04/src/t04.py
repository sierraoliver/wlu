"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import square_pyramid

base = float(input("Base of Square Pyramid: "))
height = float(input("Height of Square Pyramid: "))

sh, area, vol = square_pyramid(base, height)

print(f"Slant Height: {sh}, Area: {area}, Volume: {vol}")
