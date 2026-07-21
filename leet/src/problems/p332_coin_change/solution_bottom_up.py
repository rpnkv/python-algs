# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         sums = {0:0}
#         coins.sort(reverse=True)
#
#         for i in range(1, amount + 1):
#             for c in coins:
#                 if c > i:
#                     continue
#
#                 if i == c:
#                     sums[i] = 1
#                     continue
#
#                 if (i - c) in sums:
#                     if not i in sums:
#                         sums[i] = sums[i-c] + 1
#
#                     sums[i] = min(sums[i-c] + 1, sums[i])
#
#
#         return sums[amount] if amount in sums else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import math
        possibilities = [-1] * (amount + 1)
        possibilities[0] = 0

        for a in range(1, len(possibilities)):
            for c in coins:
                if c > a:
                    continue
                if possibilities[a - c] != -1:
                    if possibilities[a] == -1:
                        possibilities[a] = math.inf

                    possibilities[a] = min(possibilities[a], possibilities[a - c] + 1)

        return possibilities[amount]
