def threshold(length: int) -> int:
    """
    Returns index, pointing to the element in the middle of input range, checkup must stop on.
    :param length:
    :return:
    """
    return 0


def mirror_index(index: int, length: int) -> int:
    return 0


def is_palindrome(x: int) -> bool:
    num_str = str(x)
    str_len = len(num_str)

    for char_index in range(0, str_len):
        if num_str[char_index] != mirror_index(char_index, str_len):
            return False

    return True
