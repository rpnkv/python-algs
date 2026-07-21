class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue

            multiplying = []
            while stack and stack[-1].isalpha():
                multiplying.append(stack.pop())
            stack.pop()

            multiplier = []
            while stack and stack[-1].isdigit():
                multiplier.append(stack.pop())

            stack += reversed(multiplying * int("".join(reversed(multiplier))))

        return "".join(stack)


