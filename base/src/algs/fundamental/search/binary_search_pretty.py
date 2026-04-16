"""Binary Search Algorithm"""


def _narrow_boundaries(arr, target, left: int, right: int) -> tuple[int, int]:
    """
        Encapsulates boundaries shift logic.
    """
    mid = (left + right) // 2
    if arr[mid] < target:
        return mid + 1, right
    else:
        return left, mid


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
