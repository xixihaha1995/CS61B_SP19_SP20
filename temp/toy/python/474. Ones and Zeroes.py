class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]* m for _ in range(n)]

        for i in range(len(strs)):
            zeros = self.counter(strs[i], "0")
            ones = self.counter(strs[i], "1")
            for j in range(m,zeros - 1,-1):
                for k in range(n, ones -1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-zeros][k-ones])
        return dp[-1][-1]

    def counter(self, strs, num):
        res = 0
        for i in strs:
            if i == num: res += 1
        return res



