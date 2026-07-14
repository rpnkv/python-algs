class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr_target: int, prev:list[int]) -> bool:
            for num in nums:
                if curr_target - num == 0:
                    res.append(prev + [num])
                    continue

                if curr_target - num < 0:
                    continue

                dfs(curr_target - num, prev + [num])


        dfs(target, [])

        return res

if __name__ == "__main__":
    cases = [
        ([3], 5, [], "example 3N"),
        ([2,5,6,9], 9, [[2,2,5],[9]], "example1")
    ]

    for i1, i2, e, c in cases[1:]:
        a = Solution().combinationSum(i1,i2)

        assert a == e, f"failed case {c}"
