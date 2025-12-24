from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        l = 0

        while l < len(nums):
            if nums[l] == val:
                if l + 2 == len(nums):
                    return len(nums) - 1
                else:
                    r = l + 1
                    break
            l += 1

        while r < len(nums):
            if nums[r] == val:
                nums[r], nums[l] == nums[l], nums[r]
                r += 1
                l += 1
            else:
                r += 1

        return len(nums) - l
