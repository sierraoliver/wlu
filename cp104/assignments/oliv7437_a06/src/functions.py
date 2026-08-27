"""
-------------------------------------------------------
Assignment 6, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""


def total_wins():
    """
    -------------------------------------------------------
    Determines how many times purple and gold are entered.
    Use: purple, gold = total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        purple - number of times purple is entered (int)
        gold - number of times gold is entered (int)
    ------------------------------------------------------
    """
    purple = 0
    gold = 0

    colour = input("Enter the winning team: ")

    while colour != "":

        if colour == "purple":
            purple += 1

        elif colour == "gold":
            gold += 1

        colour = input("Enter the winning team: ")

    return purple, gold


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    counter = number-1
    prime = True

    if number == 1:
        prime = False

    while counter > 1:

        if (number % counter) == 0:
            prime = False

        counter -= 1

    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate/100:.2%}")
    print(f"Monthly Payment: ${payment:.2f}")
    print(f"--------------------------------")
    print(f"Month Interest  Payment  Balance")
    print(f"--------------------------------")

    balance = principal_amount
    month = 1
    percent = (interest_rate/100)/12

    while balance != 0:

        interest = balance*percent

        balance += balance*percent

        if payment > balance:
            payment = balance

        balance -= payment

        print(f"{month:5d} {interest:8.2f}  {payment:7.2f}  {balance:7.2f}")

        month += 1

    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    if number < 0:
        number *= -1

    number = number//10
    digits = 1

    while number != 0:

        number = number // 10

        digits += 1

    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    counter = 1

    while number != counter:

        if (number % counter) == 0:
            total += counter

        counter += 1

    return total
