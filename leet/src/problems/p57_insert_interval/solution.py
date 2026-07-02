class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_start, new_end = newInterval

        for start, end in intervals:
            if new_start <= end and start <= new_end:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
                continue
            else:
                res.append([start, end])

        res.append([new_start, new_end])

        res.sort(key=lambda i: i[0])

        return res


if __name__ == "__main__":
    cases = [
        # ([[1, 3], [4, 6]], [2, 5], [1, 6], "example 1"),
        # ([[1, 2], [3, 5], [9, 10]], [6, 7], [[1, 2], [3, 5], [6, 7], [9, 10]], "example 2"),
        ([[0, 1], [2, 4], [5, 7], [8, 10]], [3, 6], [[0, 1], [2, 7], [8, 10]], "my example 1"),
    ]

    sol = Solution()

    for incoming, new_interval, expected_outcome, case_id in cases:
        actual_outcome = sol.insert(incoming, new_interval)

        if actual_outcome == expected_outcome:
            print(f"case {case_id} succeeded")
