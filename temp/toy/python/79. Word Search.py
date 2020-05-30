class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.exit(board, x, y, word, 0):
                    return True
        return False
    def exit(self, board, x,y, word, i):
        if i == len(word):
            return True
        if x<0 or x >= len(board) or y <0 or y >= len(board[0]):
            return False
        if board[x][y] != word[i]:
            return False
        isexit = self.exit(board, x+1,y, word, i+1) or self.exit(board, x-1,y, word, i+1)\
        or self.exit(board, x,y+1, word, i+1) or self.exit(board, x,y-1,word, i+1)
        return isexit