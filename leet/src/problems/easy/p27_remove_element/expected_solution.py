from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        We split array to 3 zones by 2 pointers: left and right:
            - elements to the left of L aren't equal to val;
            - elements between L and R are 'val';
            - elements to the right of R aren't tested.

        After R reaches the end of the array, the algorithm is completed.

        While iterating, if R reaches non-removing value, it switches it with the most left "removing" value in the
        array.

        Left always points to the next "removing" value.


        Initial state.

        Left must be set to the first element to remove.
        Right is set to the next element to the left one.
        """

        l = 0

        while l < len(nums):
            if nums[l] == val:
                break
            else:
                l += 1
        else:
            return l

        r = l + 1

        while r < len(nums):
            if nums[r] != val:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1

            r += 1

        return l
