class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row <= rows and col >= 0:

                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else: col -= 1
            else: return False

