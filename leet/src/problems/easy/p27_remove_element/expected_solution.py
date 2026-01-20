from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            Two pointers.
            Invariants:
            - only 'valid' elements to the left from the left
            - 'invalid' elements between left and right
            - 'unknown' elements to the right from the right

            How to keep them. Thoughts only.
            1. List is processed when right pointer passes the last element
            2. Can the left pointer overtake the right one?
            No, because the right is initially ahead of the left and the right shifts at each iteration, but the left
            -- doesn't.
            3. Before the cycle begins, we set up the state by traversing the right one to the very first 'invalid'
            element.

            4. Left points to the next 'bad' element.
            If, when setting initial state, the left one has reached the end of the list -- exit.

            5. Right, at each iteration, traverses 1 element right. If it reaches 'good' element, swap.

        """

        l, r = 0, 0

        for i, n in enumerate(nums):
            if n == val:
                l = i
                break
        else:
            return l



        r = l + 1

        while r < len(nums):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            else:
                r += 1

        return l - 1
