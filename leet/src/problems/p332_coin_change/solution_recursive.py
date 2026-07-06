class Solution:
    #ready but too slow
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # if amount < 0:
        #     return -1

        coins.sort(reverse=True)

        options = []

        for coin in coins:
            if coin > amount:
                continue

            if amount - coin < 0:
                continue

            option = self.coinChange(coins, amount - coin)
            if option != -1:
                options.append(option + 1)


        return min(options) if options else -1



if __name__ == "__main__":


    for inp, inp2, exp, case_id in cases:
        actual = Solution().coinChange(inp, inp2)

        assert actual == exp, f"failed for {case_id}: e:{exp}, a:{actual}"
