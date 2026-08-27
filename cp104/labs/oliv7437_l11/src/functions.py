"""
-------------------------------------------------------
Lab 11, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# imports
import random
import string


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    each_col = []

    for r in range(0, rows):

        for c in range(0, cols):

            if value_type == "int":
                number = random.randint(low, high)

            elif value_type == "float":
                number = random.uniform(low, high)

            each_col.append(number)

        matrix.append(each_col)

        each_col = []

    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    counter = 0
    length = len(matrix)
    if length == 1:
        end = length

    else:
        end = length+1

    for x in range(0, end):
        print(f"\t{x}", end="")

    print()

    for y in range(0, length):
        print(f" {y}    ", end="")

        for s in range(0, end):
            if value_type == "float":
                print(f"\t{matrix[counter][s]:.2f}", end="")

            elif value_type == "int":
                print(f"\t{matrix[counter][s]:d}", end="")

        counter += 1
        print()

    return


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []
    each_col = []
    characters = string.ascii_letters

    for r in range(0, rows):

        for c in range(0, cols):

            letter = random.choice(characters)
            letter = letter.lower()

            each_col.append(letter)

        matrix.append(each_col)

        each_col = []

    return matrix


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """

    counter = 0
    length = len(matrix)
    col_length = len(str(matrix[0]))//5

    if col_length == 1:
        end = length

    else:
        end = col_length

    for x in range(0, end):
        print(f"\t{x}", end="")

    print()

    for y in range(0, length):
        print(f" {y}    ", end="")

        for s in range(0, end):
            print(f"\t{matrix[counter][s]}", end="")

        counter += 1
        print()

    return


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = 1000
    largest = 0
    total = 0
    numbers = 0

    rows = len(matrix)
    x = 0

    while x < rows:
        cols = len(matrix[x])
        y = 0
        while y < cols:
            number = matrix[x][y]

            if number < smallest:
                smallest = number

            if number > largest:
                largest = number

            total += number
            numbers += 1

            y += 1
        x += 1

    average = total/numbers

    return smallest, largest, total, average


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    smallest = 1000
    largest = 0

    rows = len(matrix)
    x = 0

    while x < rows:
        cols = len(matrix[x])
        y = 0
        while y < cols:
            number = matrix[x][y]

            if number < smallest:
                smallest = number
                s_position = [x, y]

            if number > largest:
                largest = number
                l_position = [x, y]

            y += 1
        x += 1

    return s_position, l_position


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    element = []
    transposed = []
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(0, cols):

        for c in range(0, rows):
            number = matrix[c][r]

            element.append(number)

        transposed.append(element)
        element = []

    return transposed
