from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None

        for n in nums:
            if element:
                if n == element:
                    count += 1
                else:
                    if count == 1:
                        count = 0
                        element = None
                    else:
                        count -= 1
            else:
                element = n
                count = 1


        return element

