from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            Let's check if "remove if match" approach will work with 'for' loop.
        """

        # for i in nums:
        #     if i == val:
        #         nums.remove(i)
        #
        #
        # return len(nums)

        """
            Doesn't work. Switching to manual iteration solution
        """

        i = 0

        while i != len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return i
