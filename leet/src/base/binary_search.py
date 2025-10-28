"""Binary Search Algorithm"""


def _narrow_boundaries(arr, target, left: int, right: int) -> tuple[int, int]:
    """
        Encapsulates boundaries shift logic.
    """
    mid = (left + right) // 2
    if arr[mid] == target:
        left = mid
        right = mid
    else:
        if arr[mid] > target:  # if searching el isn't eq to mid, then it's either gt or lt
            right = mid - 1
        else:
            left = mid + 1

    return left, right


def search_while(arr, target) -> int:
    """
        Binary search implementation, using "while" loop.
    """
    if len(arr) == 0:
        return -1

    left, right = 0, len(arr) - 1

    while left != right:
        left, right = _narrow_boundaries(arr, target, left, right)

    if arr[left] == target:
        return left
    else:
        return -1
