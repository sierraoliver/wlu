"""
-------------------------------------------------------
Lab 7, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0

    while current < target:
        current += current * (rate/100)

        years += 1

    return years


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    number = float(input("First positive value: "))
    maximum = number
    minimum = number
    total = 0
    counter = 0

    while number >= 0:

        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

        total += number

        counter += 1

        number = float(input("Next positive value: "))

    average = total / counter

    return minimum, maximum, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    expenses = float(input("Enter an expense (0 to quit): "))
    total_expenses = 0

    while expenses != 0:
        total_expenses += expenses

        expenses = float(input("Enter another expense (0 to quit): "))

    remaining_balance = available - total_expenses

    if remaining_balance > 0:
        status = "Surplus"

    elif remaining_balance < 0:
        status = "Deficit"

    else:
        status = "Balanced"

    return total_expenses, remaining_balance, status


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the highest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input(f"Enter a value between {low} and {high}: "))

    while value > high or value < low:

        if value > high:
            print("Value entered is too high")

        if value < low:
            print("Value entered is too low")

        value = int(input(f"Enter a value between {low} and {high}: "))

    return value


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    # Constants
    OVER_HOURS = 40
    EXTRA_RATE = 1.5
    GROSS_SALARY = 0.03625

    total = 0
    counter = 0

    employee_id = int(input("Employee ID: "))

    while employee_id != 0:

        wage_rate = int(input("Hourly wage rate: "))
        hours_worked = int(input("Hours worked: "))

        if hours_worked > OVER_HOURS:
            extra_hours = hours_worked - OVER_HOURS

            net_payment = (OVER_HOURS * wage_rate)

            extra_hours *= (wage_rate * EXTRA_RATE)

            net_payment += extra_hours

        else:
            net_payment = wage_rate * hours_worked

        net_payment -= (net_payment * GROSS_SALARY)

        total += net_payment

        counter += 1

        print(f"Net payment for employee {employee_id}: ${net_payment:.2f}")

        print()

        employee_id = int(input("Employee ID: "))

    average = total/counter

    return total, average
