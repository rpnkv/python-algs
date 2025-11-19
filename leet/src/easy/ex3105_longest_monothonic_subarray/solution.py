from typing import List


class Solution:
    def longestMonotonicSubarray(self, input_arr: List[int]) -> int:
        index = 1

        prev_relation: str = None

        current_len = 1

        max_len = 1

        while index < len(input_arr):
            current_relation: str

            if input_arr[index] - input_arr[index - 1] < 0:
                current_relation = "decreasing"
            elif input_arr[index] - input_arr[index - 1] > 0:
                current_relation = "increasing"
            else:
                current_relation = "equals"

            if current_relation == "equals":
                current_len = 1
            elif current_relation != prev_relation:
                current_len = 2
            else:
                current_len += 1

            if max_len < current_len:
                max_len = current_len

            prev_relation = current_relation
            index += 1

        return max_len
