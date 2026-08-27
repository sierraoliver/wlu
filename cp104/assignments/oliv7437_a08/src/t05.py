"""
-------------------------------------------------------
Assignment 8, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import has_word_chain

words = ['camel', 'lions', 'sparrow', 'wolf', 'ferret']

word_chain = has_word_chain(words)

print(f"""List: {words}
{word_chain}""")
