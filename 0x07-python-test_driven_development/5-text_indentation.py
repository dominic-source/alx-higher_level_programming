#!/usr/bin/python3

"""This module will print text before .,?

"""


def text_indentation(text):

    """Indent text with the text indentation function"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    start = 0
    flag = 1
    end = 0
    for i in text:
        end += 1
        if (i == ' ') and (flag == 1):
            start += 1
        else:
            flag = 0
            if i in ".?:":
                flag = 1
                print(text[start:end], end='')
                start = end
                print()
                print()
            elif end == len(text):
                strm = text[start:-1]
                print(strm.strip(), end='')
