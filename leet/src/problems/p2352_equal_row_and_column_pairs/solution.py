from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = {tuple(arr): arr for arr in grid}
        matching_count = 0

        for row_index in range(len(grid)):
            row = tuple(col[row_index]for col in grid)

            if row in columns and columns[row] == list(row):
                matching_count += 1

        return matching_count
