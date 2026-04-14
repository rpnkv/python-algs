from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        intervals_to_remove = [False] * len(intervals)

        for i, current_interval in enumerate(intervals):
            if intervals_to_remove[i]:
                continue

            if i == len(intervals) - 1:
                break

            current_interval_len = current_interval[1] - current_interval[0]
            j = i + 1
            next_interval = intervals[j]

            while next_interval[0] < current_interval[1]:
                next_interval_len = next_interval[1] - next_interval[0]

                if next_interval_len > current_interval_len:
                    intervals_to_remove[j] = True
                    j += 1
                    if j < len(intervals):
                        next_interval = intervals[j]
                        continue
                    else:
                        break
                else:
                    intervals_to_remove[i] = True
                    break

        res = 0
        for verdict in intervals_to_remove:
            if verdict:
                res += 1

        return res

