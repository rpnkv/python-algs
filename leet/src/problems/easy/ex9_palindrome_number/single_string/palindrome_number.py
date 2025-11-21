def threshold(length: int) -> int:
    """
    Returns index, pointing to the element in the middle of input range, checkup must stop on.
    :param length:
        input number length
    :return:
        [+1,4] (2) -> 1
        [+1,4,8] (3) -> 1
        [+1,+4,8,5] (4) -> 2
        [+1,+4,8,5,6] (5) -> 2
    """
    return length // 2


def mirror_index(index: int, length: int) -> int:
    """
    Returns index of the element on the opposite side of processing number.
    :param index: processing element index. Expects indices to the middle of the input range.
    :param length: total number length
    :return:
        For input array like: [1,4,5,4,1], having odd elements and indices [0,1,2,3,4], will produce:
        - for 0 -- 4
        - for 1 -- 3

        For input array like: [1,4,5,4], having even elements and indices [0,1,2,3], will produce:
        - for 0 -- 3
        - for 1 -- 2
    """
    return length - 1 - index


def is_palindrome(x: int) -> bool:
    num_str = str(x)
    str_len = len(num_str)

    for char_index in range(0, threshold(str_len)):
        if num_str[char_index] != num_str[mirror_index(char_index, str_len)]:
            return False

    return True
