"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-02"
-------------------------------------------------------
"""

number = int(input("Enter a positive digit number: "))

first_digit = number//10

second_digit = number % 10

difference = first_digit - second_digit

print(f"The difference of the digits of {number} is {difference}")
