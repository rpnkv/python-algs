class Solution:
    # rev2
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        pairs = 0

        for n in nums:
            target = k - n
            if target in counts and counts[target] > 0:
                counts[target] -= 1
                pairs += 1
            else:
                if n in counts:
                    counts[n] += 1
                else:
                    counts[n] = 1

        return pairs

# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         s, count = set(), 0
#
#         for n in nums:
#             target = k - n
#
#             if target in s:
#                 count += 1
#                 s.remove(target)
#             else:
#                 s.add(n)
#
#         return count


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxOperations([3,5,1,5], 2 ) == 0
    assert sol.maxOperations([3,1,3,4,3], 6 ) == 1
    assert sol.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3 ) == 4
    assert sol.maxOperations([2, 1, 1, 1, 2, 1, 2, 2, 2, 2], 3) == 4
    assert sol.maxOperations([num for num in [2, 1, 1, 1, 2, 1, 2, 2, 2, 2] if num in [2, 1]], 3) == 4
