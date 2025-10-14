"""Binary Search Algorithm"""


def _resolve_new_boundaries(arr, target, left: int, right: int) -> tuple[int, int]:
    """

    """
    return -1, -1


def _resolve_if_target_is_found():
    return False


def search_while(arr, target) -> int:
    left = 0
    right = len(arr) - 1

    while left != right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    if arr[left] == target:
        return left
    else:
        return -1
