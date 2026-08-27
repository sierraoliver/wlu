"""
-------------------------------------------------------
Lab 4, functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
import math


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """

    diam = 2 * radius

    return (diam)


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    sb = base/2

    slant_height = math.sqrt((height**2)+(sb**2))

    area = (base**2)/4 + (height**2)
    area = math.sqrt(area)
    area = (base**2) + (2*base)*area

    volume = (base**2)*(height/3)

    return(slant_height, area, volume)


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    # Constants
    NICKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25
    LOONIE = 1.00
    TOONIE = 2.00

    total = (nickels * NICKEL) + (dimes * DIME) + (quarters *
                                                   QUARTER) + (loonies * LOONIE) + (toonies * TOONIE)

    return (total)


def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
       size - current population (int >= 0)
       births - average seconds between births (int >= 0)
       deaths - average seconds between deaths (int >= 0)
       immigrants - average seconds between immigrations (int >= 0)
       years - years to calculate new population (int > 0)
    Returns:
       new_size - new population size (int)
    -------------------------------------------------------
    """
    # Constants
    SECONDS_PER_YEAR = 31536000

    births = (SECONDS_PER_YEAR // births)*years
    deaths = (SECONDS_PER_YEAR // deaths)*years
    immigrants = (SECONDS_PER_YEAR // immigrants)*years

    new_size = (size + births - deaths + immigrants)

    return(new_size)


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    # Constants
    MINUTES = 60
    HOURS = 3600
    DAYS = 86400

    minutes = seconds // MINUTES
    hours = seconds // HOURS
    days = seconds // DAYS

    return (days, hours, minutes)
