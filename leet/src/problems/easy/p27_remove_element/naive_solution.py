from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            refers to base array exercise 'remove element'
        """
        i = 0
        length=len(nums)

        while i != length:
            if nums[i] == val:
                nums.remove(nums[i])
                length -= 1
            else:
                i += 1