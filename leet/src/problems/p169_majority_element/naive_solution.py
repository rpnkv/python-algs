from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for n in nums:
            if n not in counts:
                new_count = 1
            else:
                new_count = counts[n] + 1

            counts[n] = new_count


        majority_element, majority_count = counts.popitem()

        for element, count in counts.items():
            if count > majority_count:
                majority_element= element
                majority_count = count

        return majority_element

