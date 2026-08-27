"""
-------------------------------------------------------
Assignment 9, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""


def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    data = file_handle.readline()
    line_counter = 0

    while data != "" and line_counter < count:

        print(f"{data}", end="")

        line_counter += 1

        data = file_handle.readline()

    return


def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    data = file_handle.readline()

    while data != "":

        data = data.strip().split(",")
        length = len(data)

        for x in range(1, length):
            number = int(data[x])
            number_list.append(number)

        data = file_handle.readline()

    return number_list


def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    upper = 0
    lower = 0
    digits = 0
    space = 0
    remaining = 0
    data = file_handle.readline()

    while data != "":

        length = len(data)

        # for the length of the line, checks what each is
        for x in range(0, length):
            element = data[x]

            if element.isupper():
                upper += 1

            elif element.islower():
                lower += 1

            elif element.isdigit():
                digits += 1

            elif element.isspace():
                space += 1

            else:
                remaining += 1

        data = file_handle.readline()

    return upper, lower, digits, space, remaining


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line_counter = 0
    data = fh_read.readline()

    while data != "":
        data.strip()

        line_number = [line_counter]

        fh_write.write(f"{line_number} {data} \n")

        line_counter += 1

        data = fh_read.readline()

    return


def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    lowest = 100
    highest = 0
    total = 0
    student_num = 0

    data = file_handle.readline()

    while data != "":

        data = data.strip().split(",")
        end = len(data)-1

        mark = int(data[end])

        if mark < lowest:
            lowest = mark
            lowest_id = data[end-1]

        if mark > highest:
            highest = mark
            highest_id = data[end-1]

        total += mark

        student_num += 1

        data = file_handle.readline()

    average = total/student_num

    return lowest_id, highest_id, average
