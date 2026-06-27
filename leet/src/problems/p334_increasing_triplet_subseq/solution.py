from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = c = pow(2,32)

        for n in nums:
            if n < c:
                if n < b:
                    if n < a:
                        a = n
                    else:
                        b = n
                else:
                    return True


        return False
