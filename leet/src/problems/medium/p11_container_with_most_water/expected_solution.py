from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        max_area = 0

        while True:
            current_width = r - l
            current_height = min(height[l], height[r])

            current_area = current_width * current_height
            max_area = max(current_area, max_area)

            if l + 1 == r:
                break

            if r -1 == l:
                break

            #if height[l] + 1 > height[r] - 1:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area
