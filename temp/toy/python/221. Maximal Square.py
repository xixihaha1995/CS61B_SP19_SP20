from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                print(matrix)
                if i != 0 and j != 0:
                    if matrix[i][j] != 0:
                        matrix[i][j] = str(min(int(matrix[i-1][j]), int(matrix[i][j-1])) + 1)

        return max(matrix)

if __name__ == '__main__':
    print(Solution().maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    ))