class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []

        def backtrack(board, row):
            # //以row的index为选择标尺
            if row == len(board):
                tmp_list = []
                for e_row in board:
                    tmp = ''.join(e_row)
                    tmp_list.append(tmp)
                res.append(tmp_list)
                return
            for col in range(len(board[0])):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

        def isValid(board, row, col):
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            r_row, r_col = row, col
            while r_row > 0 and r_col < n - 1:
                r_row -= 1
                r_col += 1
                if board[r_row][r_col] == 'Q':
                    return False
            l_row, l_col = row, col
            while l_row > 0 and l_col > 0:
                l_row -= 1
                l_col -= 1
                if board[l_row][l_col] == 'Q':
                    return False
            return True

        backtrack(board, 0)
        return res
