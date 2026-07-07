# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#
#         for c in s:
#             if c != ']':
#                 stack.append(c)
#                 continue
#
#             operand = []
#             while stack and stack[-1].isalpha():
#                 operand.append(stack.pop())
#
#             stack.pop() # remove '['
#             operand.reverse()
#
#             multiplier = []
#             while stack and stack[-1].isdigit():
#                 multiplier.append(stack.pop())
#
#             multiplier = int("".join(reversed(multiplier)))
#
#             stack.extend(operand * multiplier)
#
#
#         return "".join(stack)

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


