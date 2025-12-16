arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 3]

expected1 = [(1, 1), (2, 2), (3, 3), (4,)]
expected2 = [(1, 3), (2, 2), (3, 1), (4,)]
expected3 = [(1,), (2, 1), (3, 2), (4, 3)]
expected4 = [(1,), (2, 3), (3, 2), (4, 1)]


def merge1(lst1: list[int], lst2: list[int]) -> list[(int, int)]:
    lst = []

    for i1 in range(0, len(lst1)):
        lst.append((lst1[i1], lst2[i1]) if i1 < len(lst2) else (lst1[i1],))

    return lst


def merge2(lst1: list[int], lst2: list[int]) -> list[(int, int)]:
    def index_convert(i, l2) -> int:  # 1-> 3 2-> 2 3-> 1 4-> -1 1->4 2->3 3->2 4->1
        return l2 - i - 1

    lst = []

    for i1 in range(0, len(lst1)):
        i2 = index_convert(i1, len(lst2))
        lst.append((lst1[i1], lst2[i2]) if i2 >= 0 else (lst1[i1],))

    return lst


def merge3(lst1: list[int], lst2: list[int]) -> list[(int, int)]:
    def index_convert(i, l1, l2) -> int:
        return i - (l1 - l2)

    lst = []
    for i1 in range(0, len(lst1)):
        i2 = index_convert(i1, len(lst1), len(lst2))
        lst.append((lst1[i1],) if i2 < 0 else (lst1[i1], lst2[i2]))

    return lst


def merge4(lst1: list[int], lst2: list[int]) -> list[int]:
    pass


assert merge1(arr1, arr2) == expected1
assert merge2(arr1, arr2) == expected2
assert merge3(arr1, arr2) == expected3
# assert merge4(arr1, arr2) == expected4
