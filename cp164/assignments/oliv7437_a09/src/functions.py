"""
-------------------------------------------------------
Assignment 9, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-24"
-------------------------------------------------------
"""
# Imports
from Word import Word


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    text = fv.read()
    words = text.strip().replace("\n", " ").split(" ")

    for x in range(len(words)):
        data = words[x]
        data = data.lower().strip()
        if data.isalpha():
            word = Word(data)
            hash_set.insert(word)

    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    max_comp = 0
    total = 0

    for x in range(len(hash_set._table)):
        data = hash_set._table[x]
        for y in range(len(data)):
            word = data.__getitem__(y)
            comp = word.comparisons

            if comp > max_comp:
                max_comp = comp
                max_word = word

            total += comp

    return total, max_word
