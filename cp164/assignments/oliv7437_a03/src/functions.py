"""
-------------------------------------------------------
Assignment 3, Functions
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants
OPERATORS = "+-*/"


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    done = False

    while not done:

        if not source1.is_empty():
            value = source1.pop()
            target.push(value)

        if not source2.is_empty():
            value = source2.pop()
            target.push(value)

        if source1.is_empty() and source2.is_empty():
            done = True

    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    items = []
    while not source.is_empty():
        items.append(source.pop())

    for item in items:
        source.push(item)

    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    s = Stack()
    text = ""
    reversed_text = ""

    # gets rid of spaces, digits, punctuation, etc.
    length = len(string)
    for x in range(length):
        char = string[x].lower()

        if char.isalpha():
            s.push(char)
            text += char

    # gets the reverse of the original text
    while not s.is_empty():
        reversed_text += s.pop()

    # if the text is the same in reverse it is a palindrome
    if text == reversed_text:
        palindrome = True

    # else it is not
    else:
        palindrome = False

    return palindrome


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    string = string.split(" ")
    length = len(string)

    for x in range(length):
        value = string[x]

        if value.isdigit():
            s.push(value)

        elif value in OPERATORS:
            num1 = int(s.pop())
            num2 = int(s.pop())

            if value == "+":
                result = num2 + num1

            elif value == "-":
                result = num2 - num1

            elif value == "*":
                result = num2*num1

            else:
                result = num2/num1

            s.push(result)

    answer = s.pop()

    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    found_exit = False
    path = []
    s = Stack()

    key = 'Start'
    value = maze[key]

    while not found_exit:

        length = len(value)
        if length != 0:
            for x in range(length):
                letter = value[x]
                if letter not in path:
                    s.push(letter)

        if s.is_empty():
            found_exit = True
            path = None

        else:
            value = s.pop()
            path.append(value)
            key = value
            if key != 'X':
                value = maze[key]

            else:
                found_exit = True

    return path
