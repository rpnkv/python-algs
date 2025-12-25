from typing import List


def remove_element(nums: List[int], invalid_val: int) -> int:
    l = 0   # any element to the left from this position is valid
            # any element to the right from this position and to the left from 'r' position is invalid

    for r in range(len(nums)): #any element to the right may be valid or invalid
        if nums[r] != invalid_val:
            nums[l] = nums[r]
            l += 1
    return l
