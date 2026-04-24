def search(arr: list[int], target: int) -> int:
    if len(arr) == 0:
        return - 1

    l, r = 0, len(arr) - 1

    while l < r:
        mid = (r + l) // 2
        mid_el = arr[mid]
        if mid_el == target:
            return mid

        if target < mid_el:
            r = mid - 1
        else:
            l = mid + 1


    if arr[l] == target:
        return l
    else:
        return -1
