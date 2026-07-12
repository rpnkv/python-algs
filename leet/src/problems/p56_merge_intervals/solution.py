class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        res = [intervals[0]]

        for curr_start, curr_end in intervals[1:]:
            prev_start, prev_end = res[-1]

            if curr_start < prev_end:
                res[-1][1] = max(curr_start, prev_end)
            else:
                res.append([curr_start, curr_end])

        return res