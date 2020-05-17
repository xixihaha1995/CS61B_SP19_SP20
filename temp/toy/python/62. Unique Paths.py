class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maxindex = max(m,n)
        minindex = min(m,n)
        dp = [1] * (minindex)
        dp[0] = 1
        for i in range(1,maxindex):
            for j in range(1, minindex):
                dp[j] = dp[j] + dp[j-1]

        return dp[-1]

if __name__ == '__main__':
    print(Solution().uniquePaths(7,3))
