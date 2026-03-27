from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left: int = 0

        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i]:
                left = i
                break
        else:
            return len(nums)

        for i in range(left, len(nums)):
            if nums[left] == nums[i]:
                pass
            else:
                left += 1
                nums[left] = nums[i]

        return left + 1