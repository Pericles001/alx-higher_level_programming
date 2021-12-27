#!/usr/bin/python3
"""Module containing a function that prints a string in a certain format"""


def text_indentation(text):
    """ Prints a string line by line based on delimiters
        Arguments:
        @text: text to be printed
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    if len(text) == 0:
        return
    temp = text[0]
    delims = [',', ':', '?']
    for char in text:
        if char == ' ' and temp in delims:
            continue
        temp = char
        print(char, end="")
        if char in delims:
            print("\n\n", end="")
