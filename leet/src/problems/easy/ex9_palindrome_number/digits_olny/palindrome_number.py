"""
Tempest Keep was merely a setback!
"""
import math


def get_digit(number: int, digit_offset: int) -> int:
    """
    Extracts specific number digit by position.
    """
    left_divider = int(math.pow(10, digit_offset + 1))
    left_sub = number - (number // left_divider) * left_divider

    return left_sub // int(math.pow(10, digit_offset))


def define_num_length(number: int) -> int:
    """
    Defines the length of a number.
    Must be eventually replaced with non-string implementation.
    :param number:
    :return:
    """
    length = 0

    dividing = number

    while dividing > 0:
        length += 1
        dividing = int(dividing / 10)
        print(length, dividing)

    return length


def is_palindrome(x: int) -> bool:
    """
    Does something.
    :param x:
    :return:
    """
    if x <= 0:
        return False

    length = define_num_length(x)

    for char_index in range(0, length // 2):
        if get_digit(x, char_index) != get_digit(x, length - char_index - 1):
            return False

    return True
