class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                operand = []
                while stack and not stack[-1].isdigit():
                    operand.append(stack.pop())

                operand = "".join(reversed(operand[:-1]))

                multiplier = []

                while stack and stack[-1].isdigit():
                    multiplier.append(stack.pop())

                multiplier = "".join(multiplier.reverse())

                stack.extend(operand * int(multiplier))


        return "".join(stack)
