class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = asteroids[:1]

        for a in asteroids[1:]:
            # no collision conditions:
            # - signs match
            # - signs not match: new one is positive, stack non-empty and is negative
            # collision conditions:
            # - signs not match: new one is negative, stack non-empty and is positive
            if a < 0 and stack and stack[-1] > 0:
                new: int | None = a

                while (new and stack  and stack[-1] > 0):
                    if abs(new) == abs(stack[-1]):
                        stack.pop()
                        new = None
                    else:
                        if abs(new) > abs(stack[-1]):
                            stack.pop()
                        else:
                            new = None

                if new:
                    stack.append(new)

            else:
                stack.append(a)

        return stack
