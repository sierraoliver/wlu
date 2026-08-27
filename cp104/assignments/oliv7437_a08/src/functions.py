"""
-------------------------------------------------------
Assignment 8, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""


def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    length = len(sentence)
    starting = 0
    x = 1
    spaced = ""

    while x < length:
        letter = sentence[x]

        if letter.isupper():
            spaced += sentence[starting:x].lower() + " "
            starting = x

        x += 1

    spaced += sentence[starting:x+1].lower()
    spaced = spaced.capitalize()

    return spaced


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    length = len(string)

    if string.endswith("s") or string.endswith("sh") or string.endswith("ch"):
        pluralized = string + "es"

    elif string.endswith("y") and (string.endswith("ay")) == False and (string.endswith("oy")) == False:
        pluralized = string[0:length-1] + "ies"

    else:
        pluralized = string + "s"

    return pluralized


def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    comparison = True
    suffix = ""
    end1 = len(str1)-1
    end2 = len(str2)-1

    while comparison and end1 >= 0 and end2 >= 0:

        if str1[end1] == str2[end2]:
            suffix = str1[end1] + suffix
            end1 -= 1
            end2 -= 1

        else:
            comparison = False

    return suffix


def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    groups = isbn.split("-")
    # makes sure if -- is input there is no empty element
    groups = list(filter(None, groups))
    char_length = len(isbn)
    group_length = len(groups)
    start = groups[0]

    # check length
    if char_length != 17:
        is_valid = False

    # check group length
    elif group_length != 5:
        is_valid = False

    # check starting numbers
    elif not (start == "978" or start == "979"):
        is_valid = False

    # check to see they are all digits
    elif groups[-1].isdigit() == False:
        is_valid = False

    # check to see if last group is one digit
    elif len(groups[group_length-1]) != 1:
        is_valid = False

    # if it passes all tests, its true
    else:
        is_valid = True

    return is_valid


def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    length = len(words)
    word_chain = True
    x = 0

    while word_chain and x < length:

        # gets last letter of the first word
        word = words[x]
        last_letter = word[len(word)-1]

        # ensures it isn't the last word
        if (x+1) < length:

            # gets first letter of second word
            second_word = words[x+1]
            first_letter = second_word[0]

            # if they aren't equal it isn't a word chain
            if last_letter != first_letter:
                word_chain = False

        x += 1

    return word_chain
