from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = asteroids[:1]

        def will_collide(i: int) -> bool:
            return i < 0 < stack[-1]

        for a in asteroids[1:]:
            if not stack:
                stack.append(a)
                continue

            if not will_collide(a):
                stack.append(a)
                continue

            while stack and will_collide(a):
                if abs(stack[-1]) == abs(a): #mutual destruction
                    stack.pop()
                    break

                if abs(a) > abs(stack[-1]):  # new asteroid wins
                    stack.pop()                     # keep colliding
                    if not stack or not will_collide(a):                   # add element if stack
                        stack.append(a)             # got empty while this loop
                        break
                else:
                    break

        return stack




