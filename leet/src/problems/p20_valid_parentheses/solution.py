class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char not in d:
                stack.append(char)
            else:
                if not stack:
                    return False

                if stack.pop() != d[char]:
                    return False

        return len(s) == 0

if __name__ == "__main__":
    # assert Solution().isValid("(]") == False
    # assert Solution().isValid("()[]{}") == True
    assert Solution().isValid("()") == True