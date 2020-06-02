from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        maxnum = 0

        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            temp = int(matrix[i][0])
            maxnum = max(maxnum, temp)
        for j in range(n):
            temp = int(matrix[0][j])
            maxnum = max(maxnum, temp)
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    if matrix[i][j] != '0':
                        temp = min(int(matrix[i - 1][j]), int(matrix[i][j - 1]), int(matrix[i - 1][j - 1])) + 1
                        maxnum = max(maxnum, temp)
                        matrix[i][j] = str(temp)

        return maxnum ** 2

if __name__ == '__main__':
    print(Solution().maximalSquare(
        [["1", "0", "1", "0"], ["1", "0", "1", "1"], ["1", "0", "1", "1"], ["1", "1", "1", "1"]]
    ))