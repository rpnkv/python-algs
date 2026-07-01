class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i_n: int, i_t: int, sum_so_far: int) -> bool: # мемоизация не проканает -- все числа уникальны
            sum_so_far += nums[i_n]
            if


        for i, _ in enumerate(nums):
            dfs(i_n=i, i_t=0, sum_so_far=0)

        return res