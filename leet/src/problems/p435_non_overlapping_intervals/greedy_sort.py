from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Erases overlapping intervals.
        # если отсортировать интервалы по началу, все интервалы с одинаковым началом будут перекрываться. Наша задача -
        # оставить из них интервал с наименьгим концом
        intervals.sort(key=lambda i: i[0])

        removed = 0

        for i in range(1, len(intervals)):
            prev_start, prev_end = intervals[i - 1]

            curr_start, curr_end = intervals[i]

            # if curr_start == prev_start:
            #     intervals[i][1] = min(curr_end, prev_end)
            #     removed += 1

            if prev_end > curr_start:
                intervals[i][1] = min(prev_end, curr_end)
                removed += 1

        return removed

