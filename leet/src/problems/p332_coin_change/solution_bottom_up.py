class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = {0: 0}

        for coin in coins:
            dp[coin] = 1

        coins.sort(reverse=True)

        for i in range(1, amount + 1):
            if i in dp:
                continue

            for coin in coins:
                candidate = i - coin
                if candidate < 0:
                    continue

                if candidate not in dp:
                    continue

                if i not in dp:
                    dp[i] = dp[candidate] + 1
                else:
                    dp[i] = min(dp[i], dp[candidate] + 1)


        return dp[amount] if amount in dp else -1
