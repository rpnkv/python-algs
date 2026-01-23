from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        list_len = len(height)

        max_area = 0

        for i in range(list_len):
            for j in range(i + 1, list_len):

                # current_area = min(height[i], height[j]) *
                min_height = min(height[i], height[j])
                current_width = abs(i - j)

                current_area = min_height * current_width

                if current_area > max_area:
                    max_area = current_area

        return max_area
