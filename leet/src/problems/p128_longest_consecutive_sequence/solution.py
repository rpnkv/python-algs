from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = {*nums}

        heads = [num for num in nums_set if (num - 1) not in nums_set]

        current_max = 0
        for head in heads:
            current_len = 1
            current_head = head

            while (current_head + 1) in nums_set:
                current_len += 1
                current_head += 1

            if current_len > current_max:
                current_max = current_len


        return current_max