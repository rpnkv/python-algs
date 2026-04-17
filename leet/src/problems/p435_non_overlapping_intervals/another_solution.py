from typing import List
from math import inf

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        intervals_to_remove = len(intervals)

        previous_end = -inf

        for start, end in intervals:
            if previous_end <= start:
                intervals_to_remove -= 1
                previous_end = end

        return intervals_to_remove