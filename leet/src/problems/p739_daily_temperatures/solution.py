from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack must keep temperatures in increasing order (higher at the bottom)
        # pytest.param([75, 71, 69, 72], [0, 2, 1, 0], id="example 1 subarray"),
        stack = []
        answer = [0]*len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and stack[-1][1] < t:
                i_st, t_st = stack.pop()
                answer[i_st] = i - i_st

            stack.append((i,t))

        # 1: i=0, t=75
        # stack: [(0, 75)], answer: [0,0,0,0]
        #
        # 2: i=1, t=71
        # stack: [(0,75), (1,71)]
        #
        # 3: i=2, t=69
        # stack: [(0,75), (1,71), (2,69)]
        #
        # 4: i=3, t=72
        # stack:


        return answer
