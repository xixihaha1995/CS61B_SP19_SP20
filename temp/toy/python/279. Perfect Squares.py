class Solution:
    def numSquares(self, n: int) -> int:
        self.res = 0
        self.dp(n)
        return self.res

    def  dp(self, remainder):


        dp = [0] * n
        for i in range(1,n):
            for j*j in range(n):
                dp[i] = min(dp[i-1], dp[i - j*j]+1)
        return dp[-1]

if __name__ == '__main__':
    print(Solution().numSquares(13))
