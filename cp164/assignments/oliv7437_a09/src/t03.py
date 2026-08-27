"""
-------------------------------------------------------
Assignment 9, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-23"
-------------------------------------------------------
"""
# Imports
from Hash_Set_BST import Hash_Set
from functions import insert_words, comparison_total

file = open("otoos610.txt", "r", encoding="utf-8")

hash_set = Hash_Set(20)

insert_words(file, hash_set)

total_comp, max_word = comparison_total(hash_set)

print(f"""Total Comparisons: {total_comp:,d}
Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,d}""")
