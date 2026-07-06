class Solution:
    # not ready
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}


        def dfs(coins: List[int], amount: int) -> int:
            if amount < 0:
                return -1

            if amount in dp:
                return dp[amount]

            options = []
            for coin in coins:
                if coin > amount:
                    continue
                if amount - coin < 0:
                    continue

                if amount % coin == 0:
                    dp[amount] = int(amount / coin)
                    return dp[amount]

                option = dfs(coins, amount - coin)

                if option != -1:
                    dp[amount] = option + 1
                    return dp[amount]

            return min(options) if options else -1

        coins.sort(reverse=True)
        return dfs(coins, amount)
