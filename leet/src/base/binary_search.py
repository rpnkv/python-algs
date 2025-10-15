"""Binary Search Algorithm"""


def _resolve_new_boundaries(arr, target, left: int, right: int) -> tuple[int, int]:
    """

    """
    mid = (left + right) // 2
    if arr[mid] == target:
        left = mid
        right = mid
    else:
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left, right


def search_while(arr, target) -> int:
    if len(arr) == 0:
        return -1

    left = 0
    right = len(arr) - 1

    while left != right:
        left, right = _resolve_new_boundaries(arr, target, left, right)

    if arr[left] == target:
        return left
    else:
        return -1
