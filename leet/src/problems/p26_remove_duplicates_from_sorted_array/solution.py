from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two cycles:
            - external iterates left pointer;
            - internal iterates right pointer over repeating values;

        Left pointer, points to the last array's item, that all to the left, including it, are unique.
        Shift condition: when right pointer is at the element which != left element or array is over and we put left's
        element to right + 1 position

        Right pointer, seeking for current range's end, moves forward, until non-equal to the left pointer's value is
        met.
        """

        left = 0
        right = 0

        while left < len(nums):
            while right < len(nums):
                if nums[right] != nums[left]:
                    nums[right + 1] = nums[left]
                    break
                else:
                    left += 1

            right += 1

        return left
