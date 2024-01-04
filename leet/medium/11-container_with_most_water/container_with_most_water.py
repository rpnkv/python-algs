from typing import List


class Solution:
    @staticmethod
    def max_area(height: List[int]) -> int:
        max = 0

        for i, v in enumerate(height):
            for ii in range(i, len(height)):
                if ii != i:
                    # current_values = list()
                    lowest_side = height[i] if height[i] < height[ii] else height[ii]
                    container = lowest_side * (ii - i)
                    if container > max:
                        max = container

        return max


def main():
    assert Solution.max_area(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


if __name__ == "__main__":
    main()
