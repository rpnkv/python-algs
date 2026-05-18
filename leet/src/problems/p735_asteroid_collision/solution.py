from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = asteroids[:1]

        def has_same_sign(i: int, k:int) -> bool:
            return i < 0 and k < 0

        def will_collide(i: int) -> bool:
            return i < 0 and stack[-1] > 0

        for a in asteroids[1:]:
            if not stack:
                stack.append(a)
                continue

            if not will_collide(a):
                stack.append(a)
                continue


            # new asteroid, moving in opposite direction than stack can affect
            # stack i 3 ways:
            # - be destroyed by 1st el;
            # - be destroued by Nth el;
            # - destroy stack's 1st el;
            # - destroy stack's el until Nth;
            # - destroy stack content completely.

            while stack and will_collide(a):
                collided = a + stack[-1]

                if collided == 0:
                    stack.pop()
                    break

                if has_same_sign(collided, a):  # new asteroid wins
                #if collided > 0:  # new asteroid wins
                    stack.pop()                     # keep colliding
                    if not stack or not will_collide(a):                   # add element if stack
                        stack.append(a)             # got empty while this loop
                        break
                else:
                    break
                    pass # stack asteroid wins, keep going, stack condition
                    # will become false

        return stack




