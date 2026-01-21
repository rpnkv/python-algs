from typing import List


class Solution:

    def _search(self, board, i, j, word, n) -> bool:
        if i < 0:
            return False
        elif i >= len(board):
            return False
        elif j < 0:
            return False
        elif j >= len(board[i]):
            return False


        if board[i][j] == word[n]:
            if self.visited[i][j]:
                return False
            else:
                self.visited[i][j] = True

            if n == len(word) - 1:
                return True
            else:
                return any(
                    [
                        self._search(board, i, j + 1, word, n + 1),
                        self._search(board, i, j - 1, word, n + 1),
                        self._search(board, i + 1, j, word, n + 1),
                        self._search(board, i - 1, j, word, n + 1),
                    ]
                )
        else:
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.visited = []

                for x in range(len(board)):
                    self.visited.append([False] * len(board[x]))

                res = self._search(board, i, j, word, 0)
                if res:
                    return True


        return False
