class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                enc_fragment = stack.pop()
                while enc_fragment[-1] != '[':
                    enc_fragment += stack.pop()
                enc_fragment = enc_fragment[:-1][::-1]

                repeat = stack.pop()
                while stack and stack[-1] in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                    repeat += stack.pop()
                repeat: int = int(repeat[::-1])

                dec_fragment = enc_fragment * repeat
                stack += dec_fragment

        return "".join(stack)
