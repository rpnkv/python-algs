from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = asteroids[:1]

        for i in asteroids[1:]:
            if not stack:
                stack.append(i)
                continue

            if stack[-1] < 0 and i < 0:
                stack.append(i)
                continue

            if stack[-1] > 0 and i > 0 :
                stack.append(i)
                continue

            while True:
                prev = stack.pop()
                res = prev + i
                if res != 0:
                    if prev < 0 and res < 0:
                        stack.append(prev)
                    else:
                        stack.append(i)
                break

        return stack
