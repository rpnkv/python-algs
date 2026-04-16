def search(arr: list[int], target: int) -> int:
    if not arr:
        return -1

    left, right = 0, len(arr) - 1

    while left != right:
        mid = left + (right - left) // 2

        if target == arr[mid]:
            return mid

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid


    if arr[left] == target:
        return left
    else:
        return -1
