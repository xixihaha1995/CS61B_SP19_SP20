class Solution:
    def countWays(self, changes, n, x):
        dp = [0]*(x+1)
        dp[0] = 1
        for i in range(n):
            j = 0
            while j + changes[i] <= x:
                dp[j+ changes[i]] += dp[j]
                j += 1
        return dp[-1]
print(Solution().countWays(
    [5, 10, 25, 1], 4, 15
))