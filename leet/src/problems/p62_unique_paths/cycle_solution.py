class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * m

        for i_n in range(1, n):
            current = []
            for i_m in range(m):
                prev_top = prev[i_m]
                prev_left = 0 if i_m == 0 else current[i_m - 1]
                current.append(prev_top + prev_left)

            prev = current



        return current[-1]