from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval_list: interval_list[0])

        result = []

        i = 0
        while i != len(intervals):
            if i == len(intervals) - 1:
                result.append(intervals[i])
                return result

            current_interval = intervals[i]

            current_max_bound = current_interval[1]
            j = i + 1
            next_interval = intervals[j]

            while next_interval[0] <= current_max_bound:
                current_max_bound = max(next_interval[1], current_max_bound)
                j += 1
                if j == len(intervals):
                    break
                next_interval = intervals[j]

            result.append([current_interval[0], current_max_bound])
            i = j

        return result