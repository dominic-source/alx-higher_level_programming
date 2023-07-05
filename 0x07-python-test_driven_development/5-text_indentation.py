#!/usr/bin/python3

"""This module will print text before .,?

"""


def text_indentation(text=None):

    """Indent text with the text indentation function"""

    if (text is None) or not isinstance(text, str):
        raise TypeError("text must be a string")
    start = 0
    end = 0
    for i in text:
        end += 1
        if i in ".?:":
            print(text[start:end].strip(), end='')
            start = end
            print()
            print()
        elif end == len(text):
            strm = text[start:]
            print(strm.strip(), end='')
