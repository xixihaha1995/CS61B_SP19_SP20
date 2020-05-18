class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        for i in range(1, m):
            for j in range(n):
                sum = A[i-1][j]
                if j < n-1:
                    sum = min(sum, A[i-1][j-1], A[i-1][j+1])
                A[i][j] += sum
        return min(A[-1])

if __name__ == '__main__':
    print(Solution().minFallingPathSum(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ))
