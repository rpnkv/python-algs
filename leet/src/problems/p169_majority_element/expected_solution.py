from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = 0
        count = 0

        for i in nums:
            if element == i:
                count += 1
            else:
                if count == 0:
                    element = i
                else:
                    count -= 1

        return element
