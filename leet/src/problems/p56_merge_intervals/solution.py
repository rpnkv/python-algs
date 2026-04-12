from typing import List

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval_list: interval_list[0])

        result = []

        for i in range(len(intervals) - 1):
            current_interval = intervals[i]
            next_interval = intervals[i+1]

            if current_interval[1] < next_interval[0]:
                result.append(current_interval)
            else:
                raise NotImplementedError


        result.append(intervals[-1])

        return result

