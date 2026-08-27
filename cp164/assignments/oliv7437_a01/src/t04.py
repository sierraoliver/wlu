"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

file = open("text.txt", "r", encoding="utf-8")

upp, low, dig, whi, rem = file_analyze(file)

print(f"""Upper: {upp}
Lower: {low}
Digits: {dig}
White Spaces: {whi}
Remaining: {rem}
""")

file.close()
