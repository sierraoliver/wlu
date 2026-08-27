"""
-------------------------------------------------------
Lab 9, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""


def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """

    length = len(url)

    organization_type = url[(length-3):length]

    if organization_type == "com":
        url_type = "business"

    elif organization_type == "org":
        url_type = "non-profit"

    else:
        url_type = "other"

    return url_type


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    end = len(product_code)

    pc = product_code[0:3]

    pi = product_code[3:7]

    pq = product_code[7:end]

    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    end = len(product_code)
    category = False
    digits = False
    qualifiers = False

    if end > 2:
        product_category = product_code[0:3]
        category = product_category.isupper()

    if end > 6:
        product_id = product_code[3:7]
        digits = product_id.isdigit()

    if end > 7:
        product_qualifiers = product_code[7]
        qualifiers = product_qualifiers.isupper()

    return category, digits, qualifiers


def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards. Case is ignored.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    s = s.lower()
    backwards = s[::-1]

    if s == backwards:
        palindrome = True

    else:
        palindrome = False

    return palindrome


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppercase = 0
    lowercase = 0
    digits = 0
    space = 0
    x = 0
    end = len(txt)

    while x < end:
        letter = txt[x]

        if letter.isupper():
            uppercase += 1

        elif letter.islower():
            lowercase += 1

        elif letter.isdigit():
            digits += 1

        elif letter == " ":
            space += 1

        x += 1

    return uppercase, lowercase, digits, space
