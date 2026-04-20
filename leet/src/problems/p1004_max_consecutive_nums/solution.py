from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_conseq = 0
        zeroes = 0
        l = 0
        width = 0

        for r, r_el in enumerate(nums):
            if r_el != 1:
                zeroes += 1
                while zeroes > k:
                    if nums[l] == 0:
                        zeroes -=1
                    l+=1
                    width-=1

            width += 1
            max_conseq = max(max_conseq, width)

        return max_conseq + 1
