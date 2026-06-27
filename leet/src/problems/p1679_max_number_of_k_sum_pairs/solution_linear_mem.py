class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = count = 0
        r = len(nums) - 1

        while l < r:
            match nums[l] + nums[r]:
                case s if s == k:
                    l, r, count = l + 1, r - 1, count + 1
                case s if s < k:
                    l += 1
                case _:
                    r -= 1

        return count




if __name__ == "__main__":
    sol = Solution()

    # assert sol.maxOperations([3,5,1,5], 2 ) == 0
    assert sol.maxOperations([3,1,3,4,3], 6 ) == 1