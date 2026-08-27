"""
-------------------------------------------------------
Lab 8, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports
from morse import encode_morse
from BST_linked import BST
from morse import ByLetter

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
    node = ByLetter(value, code)
    s.insert(node)

text = "string"
print(f"Text: {text}")

print(f"encode_morse for text")
result = encode_morse(s, text)
print(result)
