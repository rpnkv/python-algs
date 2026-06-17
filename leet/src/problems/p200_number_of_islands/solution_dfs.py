class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        count = 0

        def dfs(row: int, col: int):
            if row < 0 or row >= rows:
                return

            if col < 0 or col >= cols:
                return

            if grid[row][col] == '1' and not visited[row][col]:
                visited[row][col] = True
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col-1)
                dfs(row, col+1)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and not visited[row][col]:
                    count += 1
                    dfs(row, col)

        return count


if __name__ == "__main__":
    cases = [
        # ([
        #      ["1", "1", "1", "1", "0"],
        #      ["1", "1", "0", "1", "0"],
        #      ["1", "1", "0", "0", "0"],
        #      ["0", "0", "0", "0", "0"]
        #  ], 1, "Example 1"),
        ([
             ["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]
         ], 3, "Example 2")
    ]

    sol = Solution()

    for incoming, expected_outcome, case_id in cases:
        actual_outcome = sol.numIslands(incoming)

        assert actual_outcome == expected_outcome, f"\tFailed for case '{case_id}': {actual_outcome}"
