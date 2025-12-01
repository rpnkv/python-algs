"""
This file contains an implementation of a part of 'merge sort' algorithm, performing mer of two sorted arrays.
"""


def merge(left: list[int], right: list[int]) -> list[int]:
    left_index, right_index = 0, 0

    result = []

    while left_index != len(left) and right_index != len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left_index != len(left):
        result += left[left_index:]

    if right_index != len(right):
        result+=right[right_index:]

    return result
