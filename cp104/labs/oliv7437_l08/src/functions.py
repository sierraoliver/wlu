"""
-------------------------------------------------------
Lab 8, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
# Imports
from random import randint, randrange, random, uniform


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    days_of_week = ["Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday", "Saturday"]

    week_name = days_of_week[d-1]

    return week_name


def get_month_name(m):
    """
    -------------------------------------------------------
    Returns the name of a month given its number.
    Use: name = get_month_name(m)
    -------------------------------------------------------
    Parameters:
        m - month number (int 1 <= m <= 12)
    Returns:
        name - matching month, 1 = "January", 12 = "December" (str)
    -------------------------------------------------------
    """
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]

    month_name = months[(m-1)]

    return month_name


def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    lotto_numbers = []
    random_number = 0

    while len(lotto_numbers) != n:
        random_number = randint(low, high)

        if random_number in lotto_numbers:
            pass

        else:
            lotto_numbers.append(random_number)

    lotto_numbers.sort()
    return lotto_numbers


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    length = len(values)
    negatives = 0
    positives = 0
    zeroes = 0
    evens = 0
    odds = 0

    for x in range(0, length):
        number = values[x]

        if number < 0:
            negatives += 1

        elif number > 0:
            positives += 1

        else:
            zeroes += 1

        if (number % 2) == 0:
            evens += 1

        else:
            odds += 1

    return negatives, positives, zeroes, evens, odds


def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    length = len(values)
    indexes = []

    for x in range(0, length):
        number = values[x]

        if number == value:
            indexes.append(x)

    return indexes


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    length = len(source1)
    target = []

    for x in range(0, length):

        sum = (source1[x])+(source2[x])

        target.append(sum)

    return target
