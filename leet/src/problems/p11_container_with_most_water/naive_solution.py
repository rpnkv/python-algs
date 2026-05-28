from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_s = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                max_s = max(
                    max_s,
                    (r-l) * min(height[l], height[r])
                )

        return max_s