from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])

        # visited = [[False] * len(grid[0])] * len(grid)
        visited = [[False] * width for _ in range(height)]

        count = 0

        def dfs(row, col) -> int:
            if row == height or row < 0:
                return 0

            if col == width or col < 0:
                return 0

            if grid[row][col] == '1' and not visited[row][col]:
                visited[row][col] = True

                dfs(row - 1, col)
                dfs(row + 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

                return 1

            else:
                return 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == "1" and not visited[row][col]:
                    count += dfs(row, col)

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
