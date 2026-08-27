"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering

text_file = open("wilde.txt", "r", encoding="utf-8")

new_text = open("wilde_numbered.txt", "w", encoding="utf-8")

line_numbering(text_file, new_text)

text_file.close()
new_text.close()
