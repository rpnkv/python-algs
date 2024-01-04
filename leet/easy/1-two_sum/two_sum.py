from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        pairs = list()
        visited = dict()

        for index, value in enumerate(nums):
            if (target - value) in visited:
                return [visited[target - value], index]

            visited[value] = index



def main():
    assert Solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution.twoSum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    main()
