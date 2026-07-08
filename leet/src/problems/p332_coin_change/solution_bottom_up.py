# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
#
#         dp = {0: 0}
#
#         for coin in coins:
#             dp[coin] = 1
#
#         coins.sort(reverse=True)
#
#         for i in range(1, amount + 1):
#             if i in dp:
#                 continue
#
#             for coin in coins:
#                 candidate = i - coin
#                 if candidate < 0:
#                     continue
#
#                 if candidate not in dp:
#                     continue
#
#                 if i not in dp:
#                     dp[i] = dp[candidate] + 1
#                 else:
#                     dp[i] = min(dp[i], dp[candidate] + 1)
#
#
#         return dp[amount] if amount in dp else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sums = {0:0}
        coins.sort(reverse=True)

        for i in range(1, amount + 1):
            for c in coins:
                if c > i:
                    continue

                if i == c:
                    sums[i] = 1
                    continue

                if (i - c) in sums:
                    if not i in sums:
                        sums[i] = sums[i-c] + 1

                    sums[i] = min(sums[i-c] + 1, sums[i])


        return sums[amount] if amount in sums else -1
