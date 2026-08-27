"""
-------------------------------------------------------
Assignment 5, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1

    for x in range(1, number+1, 1):
        product *= x

    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of number of calories burned and the total minutes run.
    Use: calories_treadmill (per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min = calories burned every 5 min (float>0)
        minutes = total number of minutes (int>0)
    Returns:
        None
    ------------------------------------------------------
    """

    for x in range(5, minutes+1, 5):
        calories = x*per_min
        print(f"{x:>3d}    {calories:5.1f}")

    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    Draws an arrow with # characters pointing up.
    Use: arrow_up (rows)
    -------------------------------------------------------
    Parameters:
        rows = number of rows (int>0)
    Returns:
        None
    ------------------------------------------------------
    """
    space = " "
    char = "#"

    print(f"{space*(rows-1)}{char}")

    for x in range(2, rows+1, 1):
        amount_of_spaces = rows-x
        print(f"{space*amount_of_spaces}{char}", end="")

        middle_space = (x*2-3)
        print(f"{space*middle_space}{char}")

    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    char = "-----"
    difference = stop_num - start_num

    print(f"   ", end="")

    # prints top bar of numbers
    for x in range(start_num, stop_num+1):
        print(f"    {x}", end="")

    print()
    print(f"   {char *(difference+1)}")

    # prints the table
    for y in range(start_num, stop_num+1):
        print(f"{y:2} |  {y*start_num:2d}", end="")

        for s in range(1, difference+1):
            print(f"   {y*(start_num+s):2d}", end="")

        print()

    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0

    for x in range(start, (count*increment)+1, increment):
        total += x

    return(total)
