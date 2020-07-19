class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda a:a[0])
        dp = [1] * len(pairs)
        ans = 1
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[j], dp[i]+1)
                    ans = max(dp[i], ans)
        return ans