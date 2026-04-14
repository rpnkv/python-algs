from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)


        for i, el in enumerate(temperatures):
            while stack and stack[-1][1] < el:
                i_st, el_st = stack.pop()
                answer[i_st] = i - i_st

            stack.append((i, el))

        return answer
