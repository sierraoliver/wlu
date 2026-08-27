"""
-------------------------------------------------------
Assignment 8, Task 2
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
from functions import comparison_total

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"
letters1 = []
letters2 = []
letters3 = []

source1 = BST()
source2 = BST()
source3 = BST()

for x in range(len(DATA1)):
    letter = Letter(DATA1[x])
    letters1.append(letter)
    letter = Letter(DATA2[x])
    letters2.append(letter)
    letter = Letter(DATA3[x])
    letters3.append(letter)

for x in range(len(DATA1)):
    source1.insert(letters1[x])
    source2.insert(letters2[x])
    source3.insert(letters3[x])

file = open("miserables.txt", "r", encoding="utf-8")
text = file.read()

do_comparisons(text, source1)
total1 = comparison_total(source1)

do_comparisons(text, source2)
total2 = comparison_total(source2)

do_comparisons(text, source3)
total3 = comparison_total(source3)

print(f"""Comparing by order: {DATA1}
Total Comparisons: {total1:,}
------------------------------------------------------------
Comparing by order: {DATA2}
Total Comparisons: {total2:,}
------------------------------------------------------------
Comparing by order: {DATA3}
Total Comparisons: {total3:,}""")

file.close()
