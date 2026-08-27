"""
-------------------------------------------------------
Lab 6, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-27"
-------------------------------------------------------
"""


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    total = 0

    for x in range(1, num+1, 2):
        total += x

    return(total)


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    # Constants
    SPACE = " "

    for x in range(1, height+1):
        amount_of_spaces = height-x
        print(f"{amount_of_spaces*SPACE}", end="")

        for y in range(1, x*2):
            print(f"{char}", end="")

        print()

    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    for x in range(n, 2, -1):
        print(f"{x} bottles of beer on the wall, {x} bottles of beer.")
        print(
            f"Take one down, pass it around, {x-1} bottles of beer on the wall")
        print(f"--")

    print(f"2 bottles of beer on the wall, 2 bottles of beer.")
    print(f"Take one down, pass it around, 1 bottle of beer on the wall")
    print(f"--")
    print(f"1 bottle of beer on the wall, 1 bottle of beer.")
    print(f"Take one down, pass it around, no more bottles of beer on the wall")

    return


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    current_salary = salary
    percent_increase = increase/100

    print(f"Age         Salary")
    print(f"------------------")
    print(f"{age}      {salary:10,.2f}")

    for x in range(age+1, 66):
        current_salary += (current_salary*percent_increase)
        print(f"{x}      {current_salary:>10,.2f}")

    return


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    number = float(input("First value: "))
    minimum = number
    maximum = number
    total = number

    for x in range(1, n, 1):
        number = float(input("Next value: "))
        total += number

        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

    average = total/n

    return (minimum, maximum, total, average)
