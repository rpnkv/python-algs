from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = len(nums)

        for i in range(len(nums)):
            if nums[i] == val:
                left = i
                break

        else:
            return left

        for right in range(left + 1, len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left