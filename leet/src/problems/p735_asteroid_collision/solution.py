class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = asteroids[:1]

        for a in asteroids[1:]:
            # no collision conditions:
            # - signs match
            # - signs not match: new one is positive, stack non-empty and is negative
            # collision conditions:
            # - signs not match: new one is negative, stack non-empty and is positive
            new: int | None = a

            while new and stack and new < 0 and stack[-1] > 0:  # collision is possible
                if abs(new) == abs(stack[-1]):  # mutual destruction
                    stack.pop()  # remove old, destroyed
                    new = None  # destroy new
                else:
                    if abs(new) > abs(stack[-1]):  # new destroys old
                        stack.pop()
                    else:
                        new = None  # old destroys new

            if new:
                stack.append(new)

        return stack
