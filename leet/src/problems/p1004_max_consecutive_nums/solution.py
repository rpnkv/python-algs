from typing import List

# width may not be required

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        width = -1

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1

            while k < 0:
                if nums[l] == 0:
                    k += 1

                l+= 1

            width = max(width, r - l)

        return width + 1 #?

