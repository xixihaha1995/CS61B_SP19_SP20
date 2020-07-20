class Solution:
    def copy(self, n, fileSize, target):
        dp = [[0, 4, 0] for _ in range(n)]
        for i in range(n):
            dp[i][1] = i
        dp[0][2] = fileSize[0]

        tmpMax = 0
        ans = []
        for i in range(1,len(fileSize)):
            dp[i][2] = fileSize[i] + dp[i-1][2]
            # curSize = dp[i][2]
            while dp[i][0] <= dp[i][1] and dp[i][2] > target:
                dp[i][0] += 1
                dp[i][2] -= fileSize[dp[i][0] - 1]

            if dp[i][2] > tmpMax and dp[i][2] <= target:
                tmpMax = dp[i][2]
                ans = dp[i]
        if not ans:
            return -1
        else:
            return ans
        # return ans if not ans else -1

print(Solution().copy(
    5, [1, 2, 3, 5, 4], 7
))
