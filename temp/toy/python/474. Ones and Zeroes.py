class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n + 1) for _ in range(m+1)]
        for word in strs:
            cal = self.countOneAndZero(word)
            zeros = cal[0]
            ones = cal[1]
            for i in range(m,zeros-1,-1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[-1][-1]
    def countOneAndZero(self, word):
        res = [0,0]
        for charac in word:
            if charac == '0':
                res[0] += 1
            else:
                res[1] += 1
        return res

