from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda lst: lst[0])

        if len(intervals) == 1:
            return 0

        l = removed = 0

        for r, r_int in enumerate(intervals):
            if r == 0:
                continue

            if r_int[0] != intervals[l][0] and r_int[1] > intervals[l][1]:
                l = r
            else:
                if intervals[l][1] > r_int[1]:
                    l = r
                    removed += 1
                else:
                    removed += 1
                    pass

        return removed
