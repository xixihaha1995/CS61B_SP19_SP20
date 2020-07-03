class Solution:
    def countWays(self, changes, count, amount):
        changes.sort()
        dp = [[0] *(amount + 1) for _ in range(count)]
        for i in range(count):
            dp[i][0] = 1
        j = 1
        while j * changes[0] < amount:
            dp[0][ j * changes[0]] = 1
            j += 1
        for i in range(1, count):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-changes[i]]
        return dp[-1][-1]
print(Solution().countWays(

))