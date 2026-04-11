from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        middle = float('inf')

        for current_num in nums:
            if current_num > middle:
                return True

            if current_num < smallest:
                smallest = current_num
            elif current_num < middle and current_num > smallest:
                middle = current_num

        return False
