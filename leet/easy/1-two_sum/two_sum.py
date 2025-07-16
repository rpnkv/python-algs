from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int] | None:
        tuples = dict(zip(nums, range(0, len(nums))))

        for num_index in range(0, len(nums)):
            expected_pair = target - nums[num_index]
            if expected_pair in tuples and tuples[expected_pair] != num_index:
                return [num_index, tuples[target - nums[num_index]]]


def main():
    assert Solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution.twoSum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    main()
