class Solution:
    # v2
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols, rows = len(board), len(board[0])


        def dfs(col:int, row:int, i) -> bool:
            if i == len(word):
                return True

            if col < 0 or col == cols or row < 0 or row == rows or board[col][row] != word[i] :
                return False

            board[col][row] = "*"
            res = (
                    dfs(col + 1, row, i + 1) or
                    dfs(col - 1, row, i + 1) or
                    dfs(col, row + 1, i + 1) or
                    dfs(col, row - 1, i + 1)
            )

            board[col][row] = word[i]
            return res



        for c in range(cols):
            for r in range(rows):
                if dfs(c, r, 0):
                    return True

        return False

if __name__ == "__main__":
    assert Solution().exist(
        # board = [
        #     ["A","B","C","D"],
        #     ["S","A","A","T"],
        #     ["A","C","A","E"]
        # ],
        # word = "CAT"
        board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        word="ABCCED"
    ) == True