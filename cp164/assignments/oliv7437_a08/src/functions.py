"""
-------------------------------------------------------
Assignment 8, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
from Letter import Letter


def do_comparisons(text, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    for x in range(len(text)):
        letter = text[x]
        letter = letter.upper()

        if letter.isalpha():
            data = Letter(letter)

            bst.retrieve(data)

    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    values = bst.inorder()

    for x in range(len(values)):
        total += values[x].comparisons

    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total = 0
    values = bst.inorder()

    print(f"Letter Count/Percent Table")
    print()

    for x in range(len(values)):
        total += values[x].count

    print(f"Total Count: {total:,}")
    print()

    print(f"Letter   Count       %")
    print(f"----------------------")

    for x in range(len(values)):
        letter = values[x].letter
        count = values[x].count
        percent = (count/total)
        print(f"{letter:>5s} {count:>8,d}  {percent:>6.2%}")
