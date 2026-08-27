"""
-------------------------------------------------------
Lab 5, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    # Constants
    HEAVY = 1000
    LIGHT = 10
    GRAVITY = 9.8

    weight = mass * GRAVITY

    if weight > HEAVY:
        text = ("heavy")

    elif weight < LIGHT:
        text = ("light")

    else:
        text = ("average")

    return weight, text


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    # find difference between target and value 1
    if target > v1:
        first_difference = target-v1

    else:
        first_difference = v1-target

    # find difference between target and value 2
    if target > v2:
        second_difference = target-v2

    else:
        second_difference = v2-target

    # determine which value is closer to target
    if first_difference <= second_difference:
        close_value = v1

    else:
        close_value = v2

    return close_value


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    if speed > 117:
        category = "Hurricane"

    elif speed >= 89:
        category = "Whole Gale"

    elif speed >= 62:
        category = "Gale Winds"

    elif speed >= 39:
        category = "Strong Wind"

    elif speed > 0:
        category = "Breeze"

    else:
        category = "Unknown"

    return category


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # Constants
    SALARY = 30000
    YEARS = 5

    employed = int(input("Years employed: "))

    if (employed >= YEARS):
        salary = float(input("Salary: "))

        if (salary >= SALARY):
            qualified = True

        else:
            qualified = False

    else:
        qualified = False

    return qualified


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    # constants
    BURGER_PRICE = 6.00
    WING_PRICE = 8.00
    FRY_COMBO = 1.50
    SALAD_COMBO = 2.00

    main_order = input("Order | B - burger or W - wings: ")

    if main_order == "B":
        price = BURGER_PRICE

    else:
        price = WING_PRICE

    combo = input("Make it a combo? (Y/N): ")
    if combo == "Y":
        combo_type = input("Add | F - fries or S - salad: ")

        if combo_type == "F":
            price += FRY_COMBO

        else:
            price += SALAD_COMBO

    return price
