class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        def sum() -> int:
            return numbers[l] + numbers[l]

        while r < len(numbers):
            if sum() == target:
                return [i + 1 for i in [l, r]]

            if sum() < target:
                r += 1
            else:
                l += 1
