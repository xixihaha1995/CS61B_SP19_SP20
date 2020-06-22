from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        p = [0.0] * (n + 1)
        for i in range(n):
            p[i+1] = p[i]+A[i]

        dp = [0.0] * n
        for i in range(n):
            dp[i] = (p[n] - p[i])/(n-i)

        for k in range(K-1):
            for i in range(n):
                for j in range(i+1,n):
                    dp[i] = max(dp[i], dp[j] + (p[j] - p[i])/(j-i))
        return dp[0]

print(Solution().largestSumOfAverages(
    [9,1,2,3,9], 3
))