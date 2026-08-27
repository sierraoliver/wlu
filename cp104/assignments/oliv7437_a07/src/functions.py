"""
-------------------------------------------------------
Assignment 7, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""


def list_factors(number):
    """
    -------------------------------------------------------
    Returns a list of the factors of a certain number.
    Use: list = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - int > 0
    Returns:
        list - list of factors of number (list of int)
    ------------------------------------------------------
    """
    x = 1
    list = []

    while x < number:

        if (number % x) == 0:
            list.append(x)

        x += 1

    return list


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []

    number = int(input("Enter a positive number: "))

    while number != 0:

        if number > 0:
            number_list.append(number)

        number = int(input("Enter a positive number: "))

    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    length = len(numbers)
    index_list = []

    for x in range(0, length):
        number = numbers[x]

        if number == target_number:
            index_list.append(x)

    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    x = 0
    length = len(minuend)
    target_number = subtrahend[0]

    while x < length:
        number = minuend[x]

        if number == target_number:
            minuend.pop(x)
            length -= 1

        else:
            x += 1

    return


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    index_counter = 0
    length = len(numbers)
    sorted = True
    index = -1

    while sorted and index_counter < length:

        if (index_counter+1) < length:
            num_1 = numbers[index_counter]
            num_2 = numbers[index_counter + 1]

        if num_1 > num_2:
            sorted = False
            index = index_counter + 1

        index_counter += 1

    return sorted, index
