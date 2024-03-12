def max_lower_or_equal(sorted_arr, value):
    # Сначала проверим, существует ли искомый элемент
    if not sorted_arr or sorted_arr[0] > value:
        return -1

    left_idx, right_idx = 0, len(sorted_arr)
    while left_idx + 1 < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_arr[mid_idx] <= value:
            left_idx = mid_idx
        else:
            right_idx = mid_idx
    return left_idx


def main():
    r = range(1, 6)

    for v in r:
        print(v)

    l = list(r)

    print(max_lower_or_equal(l, 3))


if __name__ == "__main__":
    main()
