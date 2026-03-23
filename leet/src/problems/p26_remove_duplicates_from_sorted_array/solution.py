from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left: int = None

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                left = i
                break

        else:
            return len(nums)

        right = left + 1

        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

            right += 1

        return left + 1
