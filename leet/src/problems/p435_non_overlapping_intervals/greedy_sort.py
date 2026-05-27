from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda lst: lst[0])

        removed = 0
        l = intervals[0]

        for r in intervals[1:]:
            if l[1] <= r[0]:
                l = r
            else:
                removed += 1
                if r[1] < l[1]:
                    l = r

        return removed
