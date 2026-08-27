"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports
from Letter import Letter
from BST_linked import BST
from functions import do_comparisons
from functions import letter_table

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters1 = []
source1 = BST()

for x in range(len(DATA1)):
    letter = Letter(DATA1[x])
    letters1.append(letter)

for x in range(len(DATA1)):
    source1.insert(letters1[x])

file = open("miserables.txt", "r", encoding="utf-8")
text = file.read()

do_comparisons(text, source1)
letter_table(source1)

file.close()
