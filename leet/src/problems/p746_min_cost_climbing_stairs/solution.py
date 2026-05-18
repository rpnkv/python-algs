from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_cache: dict[int, int] = {}

        def climb(pos: int, curr_cost: int) -> int:
            if pos >= len(cost):
                return curr_cost
            else:
                cost1 = climb(pos + 1, cost[pos] + curr_cost)
                cost2 = climb(pos + 2, cost[pos] + curr_cost)
                return min(
                    cost1, cost2
                )

        climb0 = climb(0, 0)
        climb1 = climb(1, 0)

        return min(climb0, climb1)
