from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            m = 0
            n = 0
        else:
            m = len(matrix)
            n = len(matrix[0])
        self.sumM = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.sumM[i+1][j+1] = self.sumM[i+1][j] + self.sumM[i][j+1] - self.sumM[i][j] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumM[row2 + 1][col2 + 1] - self.sumM[row2+1][col1] - self.sumM[row1][col2+1] + self.sumM[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)