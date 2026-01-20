from typing import List


# frame 1: (2, 1, 0, '(') if 2 call generate(2, 1, 0, '((') frame 2
# frame 2: (2, 2, 0, '((') if 3 call generate(2, 2, 1, '(()') frame 3
# frame 3: (2, 2, 1, '(()') if 3 call generate(2, 2, 2, '(())') frame 4
# frame 4: (2, 2, 2, '(())') if 1 --print('(())') method is over return to frame 3
# frame 3: method is over return to frame 2
# frame 2: method is over return to frame 1
# frame 1: (2, 1, 0, '(') if 3 call generate (2, 1, 1, '()') frame 5
# frame 5: (2, 1, 1, '()') if 2 call generate (2, 2, 1, '()(') frame 6
# frame 6: (2, 2, 1, '()(') if 3 call generate (2, 2, 2, '()()') frame 7
# frame 7: (2, 2, 2, '()()') if 1 print('()()') return to frame 6
# frame 6: method is over return to frame 5
# frame 5: if 3 not match method is over return to frame 1
# frame 3: method is over
class Solution:

    def __init__(self):
        self.res = []

    def generate(self, total: int, left: int, right: int, acc: list[str]) -> List[str]:
        # if 1
        if left == right == total:
            self.res.append(''.join(acc))

        # if 2
        if left != total:
            acc.append('(')
            self.generate(total, left + 1, right, acc)
            acc.pop()

        # if 3
        if right != total and right < left:
            acc.append(')')
            self.generate(total, left, right + 1, acc)
            acc.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.generate(n, 1, 0, ['('])
        return self.res


def main():
    assert Solution().generateParenthesis(1) == ["()"]
    assert Solution().generateParenthesis(2) == ["()()", "(())"]
    assert Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


if __name__ == '__main__':
    main()
