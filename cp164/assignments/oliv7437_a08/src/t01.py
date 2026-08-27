"""
-------------------------------------------------------
Assignment 8, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

s = BST()
s2 = BST()

values = [11, 22, 33, 44]
data = []

for x in range(len(values)):
    s.insert(values[x])

for x in range(len(data)):
    s2.insert(data[x])

# testing remove
source = s.levelorder()
print(f"Source: {source}")
num = 22
remove = s.remove(num)
print(f"Removing {remove}")
data = s.levelorder()
print(f"Source: {data}")

# testing eq
"""
equals = s == s2
source1 = s.levelorder()
source2 = s2.levelorder()
print(f"Source1: {source1}")
print(f"Source2: {source2}")
print(f"Equals: {equals}")
"""

# testing is_balanced
"""
b = s.is_balanced()
source = s.levelorder()
print(f"Source: {source}")
print(f"Is balanced: {b}")
"""

# testing is_valid
"""
b = s.is_valid()
source = s.levelorder()
print(f"Source: {source}")
print(f"Is valid: {b}")
"""

# testing min
"""
value = s.min()
source = s.levelorder()
print(f"Source: {source}")
print(f"Min: {value}")
"""

# testing leaf_count
"""
count = s.leaf_count()
source = s.levelorder()
print(f"Source: {source}")
print(f"Count: {count}")
"""

# testing one_child_count
"""
count = s.two_child_count()
source = s.levelorder()
print(f"Source: {source}")
print(f"Count: {count}")
"""

# testing inorder
"""
source = s.inorder()
print(f"Made from: {values}")
print(f"In order: {source}")
"""

# testing preorder
"""
source = s.preorder()
print(f"Made from: {values}")
print(f"Pre order: {source}")
"""

# testing postorder
"""
source = s.postorder()
print(f"Made from: {values}")
print(f"Post order: {source}")
"""

# testing levelorder
"""
source = s.levelorder()
print(f"Made from: {values}")
print(f"Level order: {source}")
"""
