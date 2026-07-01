class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue

            operand = []
            while stack and stack[-1].isalnum():
                operand.append(stack.pop())

            stack.pop() # remove '['
            operand.reverse()

            multiplier = []
            while stack and stack[-1].isdigit():
                multiplier.append(stack.pop())

            multiplier = int("".join(reversed(multiplier)))

            stack.extend(operand * multiplier)


        return "".join(stack)
