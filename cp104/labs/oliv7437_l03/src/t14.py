"""
-------------------------------------------------------
Lab 3, Task 14
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-09-11"
-------------------------------------------------------
"""
# Imports

# Constants
HOURS = 60
DAY = 24
MINUTES_IN_DAY = 1440

minutes = int(input("Enter number of minutes: "))

days = (minutes//HOURS) // DAY

left_over_minutes = minutes - (days*MINUTES_IN_DAY)

hours = left_over_minutes // HOURS

left_over_minutes -= (hours*HOURS)

print(f"There are {days:d} days, {hours:d} hours, and {left_over_minutes:d} minutes in {minutes:d} minutes")
