from typing import List


class Solution:
    def _search(self, board, i, j, word, n, visited: list[list[bool]]) -> bool:
        if i < 0:
            return False
        elif i >= len(board):
            return False
        elif j < 0:
            return False
        elif j >= len(board[i]):
            return False

        if board[i][j] == word[n]:
            if visited[i][j]:
                return False
            else:
                visited[i][j] = True

            if n == len(word) - 1:
                return True

            if self._search(board, i, j + 1, word, n + 1, visited.copy()):  # go right
                return True

            if self._search(board, i, j - 1, word, n + 1, visited.copy()):  # go_left
                return True

            if self._search(board, i + 1, j, word, n + 1, visited.copy()):  # go_down
                return True

            if self._search(board, i - 1, j, word, n + 1, visited.copy()):  # go_up
                return True

            visited[i][j] = False
            return False


        else:
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = []

                for x in range(len(board)):
                    visited.append([False] * len(board[x]))

                res = self._search(board, i, j, word, 0, visited)
                if res:
                    return True

        return False
