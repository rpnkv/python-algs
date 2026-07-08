# class Solution:
#     # v2
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         intervals.sort()
#         res = []
#
#         i = 0
#
#         new_start, new_end = newInterval
#
#         while i < len(intervals):
#             curr_start, curr_end = intervals[i]
#             if curr_end < new_start: # if current ends before inserting start
#                 res.append(intervals[i])
#                 i+=1
#             else:
#                 break
#
#         while i < len(intervals):
#             curr_start, curr_end = intervals[i]
#             if curr_start < new_end:
#                 new_start = min(curr_start, new_start)
#                 new_end = max(curr_end, new_end)
#                 i+=1
#             else:
#                 break
#
#         res.append([new_start, new_end])
#
#         res.extend(intervals[i:])
#
#         return res

import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_start, new_end = newInterval

        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]

            if new_start < curr_start < new_end or new_start < curr_end < new_end:
                break
            else:
                res.append(intervals[i])
        else:
            intervals.append(newInterval)
            return intervals

        while i < len(intervals) and new_end > intervals[i][0]:
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1], new_end)

            i += 1

        res.append([new_start, new_end])
        res += intervals[i:]

        return res



if __name__ == "__main__":
    cases = [
        ([[1, 3], [4, 6]], [2, 5], [[1, 6]], "example 1"),
        ([[1, 2], [3, 5], [9, 10]], [6, 7], [[1, 2], [3, 5], [6, 7], [9, 10]], "example 2"),
        ([[0, 1], [2, 4], [5, 7], [8, 10]], [3, 6], [[0, 1], [2, 7], [8, 10]], "my example 1"),
    ]

    sol = Solution()

    for incoming, new_interval, expected_outcome, case_id in cases:
        actual_outcome = sol.insert(incoming, new_interval)
        actual_outcome.sort(key=lambda i: i[0])

        if actual_outcome == expected_outcome:
            print(f"case {case_id} succeeded")
        else:
            print(f"case {case_id} failed")