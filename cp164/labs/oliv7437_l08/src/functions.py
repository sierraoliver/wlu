"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""


def node(current):

    if current is not None:

        l_node = current._left
        if l_node is not None:
            print(l_node._value)

        r_node = current._right
        if r_node is not None:
            print(r_node._value)

        node(l_node)
        node(r_node)

    return
