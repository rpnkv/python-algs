class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                accumulator = []
                while stack[-1] != '[':
                    accumulator.append(stack.pop())
                stack.pop()
                accumulator.reverse()

                num = []
                while stack and stack[-1].isnumeric():
                    num.append(stack.pop())

                num = int("".join(reversed(num)))

                stack += accumulator * num
            else:
                stack.append(char)

        return "".join(stack)