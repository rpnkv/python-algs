# v4
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval

        res = []

        i = 0
        while i < len(intervals) and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1


        while i < len(intervals) and intervals[i][0] <= new_end:
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1], new_end)
            i+=1


        res.append([new_start, new_end])
        res += intervals[i:]

        return res


if __name__ == "__main__":
    cases = [
        (
            [[1, 3], [4, 6]],
            [2, 5],
            [[1, 6]], "example 1"),

        (
            [[1, 2], [3, 5], [9, 10]],
            [6, 7],
            [[1, 2], [3, 5], [6, 7], [9, 10]], "example 2"),
        (
            [[0, 1], [2, 4], [5, 7], [8, 10]],
            [3, 6],
            [[0, 1], [2, 7], [8, 10]], "my example 1"),
    ]

    sol = Solution()

    for incoming, new_interval, expected_outcome, case_id in cases:
        actual_outcome = sol.insert(incoming, new_interval)
        actual_outcome.sort(key=lambda i: i[0])

        assert actual_outcome == expected_outcome, f"case {case_id} failed; a/e: {actual_outcome}/{expected_outcome}"

