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
        for i in range(m + 1):
            for j in range(n+1):
                self.sumM[i][j] =


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)