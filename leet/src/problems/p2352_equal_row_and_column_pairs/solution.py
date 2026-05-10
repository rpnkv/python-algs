from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = {}

        for column in grid:
            c_tuple = tuple(column)
            if c_tuple not in columns:
                columns[c_tuple] = [column]
            else:
                columns[c_tuple].append(column)


        matching_count = 0

        for row_index in range(len(grid)):
            row = tuple(col[row_index]for col in grid)

            if row in columns:
                same_hash_cols = columns[row]
                for col in same_hash_cols:
                    if col == list(row):
                        matching_count += 1

        return matching_count
