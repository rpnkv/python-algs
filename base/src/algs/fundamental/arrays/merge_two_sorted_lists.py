"""
Leetcode easy P88, but not "in place".
"""


def merge(list1: list[int], list2: list[int]) -> list[int]:
    res = []

    l1 = l2 = 0

    while l1 < len(list1) and l2 < len(list2):
        if list1[l1] < list2[l2]:
            res.append(list1[l1])
            l1 += 1
        else:
            res.append( list2[l2])
            l2 += 1

    res += list1[l1:]
    res += list2[l2:]

    return res
