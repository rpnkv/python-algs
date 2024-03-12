from typing import List


class Solution:

    @staticmethod
    def generate(total: int, left: int, right: int, acc: str) -> List[str]:
        if left != total - 1:
            return Solution.generate(6, left + 1, right, acc + '(')
        else:
            if right != total -1:
                
        if right != total - 1:
            pass

    @staticmethod
    def generateParenthesis(n: int) -> List[str]:
        list(Solution.generate(n, 0, 0, ''))


def main():
    assert Solution().generateParenthesis(1) == ["()"]
    assert Solution().generateParenthesis(2) == ["(())", "()()"]
    assert Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


if __name__ == '__main__':
    main()
