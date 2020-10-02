from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]* (n + 1) for _ in range(m + 1)]

        for i in range(len(strs)):
            zeros = self.counter(strs[i], "0")
            ones = self.counter(strs[i], "1")
            for j in range(m,zeros - 1,-1):
                for k in range(n, ones -1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-zeros][k-ones] + 1)
        return dp[-1][-1]

    def counter(self, strs, num):
        res = 0
        for i in strs:
            if i == num: res += 1
        return res

print(Solution().findMaxForm(
    ["10","0001","111001","1","0"], 5, 3
))


