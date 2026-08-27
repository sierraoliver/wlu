"""
-------------------------------------------------------
Assignment 3, Task 7
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze

maze = {'Start': ['A'], 'A': []}

print(f"Maze: {maze}")

path = stack_maze(maze)

print(f"Path: {path}")
