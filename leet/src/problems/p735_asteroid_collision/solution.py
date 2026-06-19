class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                match stack[-1] + a:
                    case x if x == 0: # nobody wins
                        a = 0
                        stack.pop()
                    case x if x > 0: # stack wins
                        a = 0
                    case x if x < 0: # incoming asteroid wins
                        stack.pop()


        return stack


