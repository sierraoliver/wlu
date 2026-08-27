"""
-------------------------------------------------------
Assignment 1, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    counter = 0
    used_values = []
    length = len(values)

    while counter != length:
        value = values[counter]

        if value in used_values:
            values.pop(counter)
            length -= 1

        else:
            used_values.append(value)
            counter += 1

    return


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    counter = 0
    length = len(minuend)

    while counter != length:

        value = minuend[counter]

        if value in subtrahend:
            minuend.pop(counter)
            length -= 1

        else:
            counter += 1

    return


def dsmvwl(string):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(string)
    -------------------------------------------------------
    Parameters:
       string - a string (str)
    Returns:
       out - string with the vowels removed (str)
    -------------------------------------------------------
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    out = ""
    length = len(string)

    for x in range(length):
        letter = string[x]

        if letter not in vowels:
            out += letter

    return out


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    data = fv.read()
    length = len(data)

    counter = 0
    upper = 0
    lower = 0
    digit = 0
    space = 0
    rem = 0

    while counter != length:
        value = data[counter]

        if value.isupper():
            upper += 1

        elif value.islower():
            lower += 1

        elif value.isdigit():
            digit += 1

        elif value.isspace():
            space += 1

        else:
            rem += 1

        counter += 1

    return upper, lower, digit, space, rem


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False

    if (year % 4) == 0:
        leap_year = True

        if (year % 100) == 0 and (year % 400) == 0:
            leap_year = True

        elif (year % 100) == 0:
            leap_year = False

    return leap_year


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True
    length = len(name)

    begin = name[0]

    # check if the beginning is a letter or underscore
    if begin == ("_") or begin.isalpha():
        valid = True

    else:
        valid = False

    # if the beginning does not match it will skip checking the rest
    if valid == True:

        for x in range(length):

            value = name[x]

            # check to see if the value is not a letter, number or underscore
            if value.isalnum() == False and value != ("_"):
                valid = False

    return valid


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    length = len(a)
    md = 0

    for x in range(length-1):
        num1 = a[x]
        num2 = a[x+1]

        difference = num1-num2

        # ensures the difference is positive
        if difference < 0:
            difference *= -1

        if difference > md:
            md = difference

    return md


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = 100000
    large = 0
    total = 0
    counter = 0
    cols = len(a)

    for x in range(cols):

        rows = len(a[x])

        for y in range(rows):
            value = a[x][y]

            if value < small:
                small = value

            if value > large:
                large = value

            total += value
            counter += 1

    average = total/counter

    return small, large, total, average


def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b) and len(a[0]) == len(b[0])

    c = []
    sum_list = []
    cols = len(a)

    for x in range(cols):

        rows = len(a[x])

        for y in range(rows):

            num1 = a[x][y]
            num2 = b[x][y]

            s = num1 + num2

            sum_list.append(s)

        c.append(sum_list)
        sum_list = []

    return c
