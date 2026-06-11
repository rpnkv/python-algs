class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for a in asteroids[1:]:
            # when asteroids collide?
            # - positive in stack and negative 'a'
            # - or negative 'a' and positive stack

            while stack and (a < 0 and stack[-1] > 0):
                c = a + stack[-1]

                match c:
                    case 0:
                        stack.pop()
                        a = 0
                    case x if x < 0:
                        stack.pop()
                    case x if x > 0:
                        a = 0

            if a != 0:
                stack.append(a)

        return stack