"""
-------------------------------------------------------
Lab 10, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    found_id = False
    result = []
    element = ""
    x = 0

    data = fh.readline()

    while data != "" and found_id == False:
        element = data[x]

        # determines the id (string before the first comma)
        while element != ",":
            x += 1
            element = data[x]

        customer_id = data[0:x]

        # if the id is the same as the one on that line
        if id_number == customer_id:
            found_id = True
            result = data.strip().split(",")

        else:
            data = fh.readline()

        x = 0

    return result


def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    maximum = 0
    x = 0

    numbers = fh.readlines()
    length = len(numbers)

    while x < length:
        numbers[x].strip()
        number = int(numbers[x])

        if number > maximum:
            maximum = number

        x += 1

    write = str(maximum) + "\n"
    fh.write(write)

    return maximum


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    counter = 0
    number = fh.readline()

    while number != "":
        number = int(number.strip())

        if number == value:
            counter += 1

        number = fh.readline()

    return counter


def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    high_length = 0
    data = fh.readline()
    word_length = len(data)

    while data != "":

        if word_length >= high_length:
            high_length = word_length
            word = data

        data = fh.readline()
        word_length = len(data)

    word = word.strip()

    return word


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    counter = 0
    word = fh_1.readline()
    word = word.strip()

    while word != "" and counter < n:

        fh_2.write(word + "\n")

        word = fh_1.readline()
        word = word.strip()

        counter += 1

    return
