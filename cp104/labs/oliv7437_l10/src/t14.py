"""
-------------------------------------------------------
Lab 10, Task 14
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import file_copy_n

words_file = open("words.txt", "r", encoding="utf-8")
new_words_file = open("new_words.txt", "a", encoding="utf-8")

value = int(input("Number of lines to copy: "))

file_copy_n(words_file, new_words_file, value)

words_file.close()
new_words_file.close()
