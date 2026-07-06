class Solution:
    # not ready too
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}

        def dfs(amount: int) -> int:
            if amount < 0:
                return -1

            if amount in dp:
                return dp[amount]

            best = -1

            for coin in coins:
                if coin > amount:
                    continue

                if amount - coin < 0:
                    continue

                res = dfs(amount - coin)
                if res != -1:
                    best = min(res+ 1, best)

            dp[amount] = best
            return best

        coins.sort(reverse=True)
        return dfs(amount)
