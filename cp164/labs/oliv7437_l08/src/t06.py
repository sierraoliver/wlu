"""
-------------------------------------------------------
Assignment 8, Task 6
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports
from morse import decode_morse
from BST_linked import BST
from morse import ByCode

s = BST()

letters = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
           ('D', '-..'), ('E', '.'), ('F', '..-.'),
           ('G', '--.'), ('H', '....'), ('I', '..'),
           ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
           ('M', '--'), ('N', '-.'), ('O', '---'),
           ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
           ('S', '...'), ('T', '-'), ('U', '..-'),
           ('V', '...-'), ('W', '.--'), ('X', '-..-'),
           ('Y', '-.--'), ('Z', '--..'))

for letter in letters:
    value = letter[0]
    code = letter[1]
    node = ByCode(value, code)
    s.insert(node)

morse = "... --- ..."
print(f"Morse: {morse}")

print(f"decode_morse for text")
result = decode_morse(s, morse)
print(result)
