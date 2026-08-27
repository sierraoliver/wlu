"""
-------------------------------------------------------
Lab 10, Task 11
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import find_longest

word_file = open("words.txt", "r", encoding="utf-8")

word = find_longest(word_file)

print(f"{word} is the last word with the longest length")

word_file.close()
