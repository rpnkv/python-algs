class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        islands = 0

        def dfs(row:int, col: int):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != "1":
                return

            grid[row][col] = "0"

            dfs(row+1, col)
            dfs(row, col+1)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1

        return islands


if __name__ == "__main__":
    cases = [
        ([
             ["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]
         ], 1, "Example 1"),
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

    print("-- success!")
