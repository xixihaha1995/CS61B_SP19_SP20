class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maxindex = max(m,n)
        minindex = min(m,n)
        dp = [1] * (minindex)
        dp[0] = 1
        for i in range(1,maxindex):
            dp[i] = dp[i] + dp [i-1]
