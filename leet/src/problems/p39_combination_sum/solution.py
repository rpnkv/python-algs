class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i:int, curr: list[int], total: int) -> None:
            if total == target:
                res.append(curr.copy())

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                else:
                    curr.append(nums[j])
                    dfs(j, curr, total + nums[j])
                    curr.pop()


        dfs(0, [], 0)

        return res


if __name__ == "__main__":
    cases = [
        ([3], 5, [], "example 3N"),
        ([2, 5, 6, 9], 9, [[2, 2, 5], [9]], "example 1")
    ]

    for i1, i2, e, c in cases[1:]:
        a = Solution().combinationSum(i1, i2)

        assert a == e, f"failed case {c}"
