from easy._9_palindrome_number.single_string.palindrome_number import threshold


def is_palindrome(x: int) -> bool:
    num_str = str(x)
    num_str_reversed = num_str[::-1]

    for char_index in range(0, threshold(len(num_str))):
        if num_str[char_index] != num_str_reversed[char_index]:
            return False

    return True
