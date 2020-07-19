class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(lambda a:a[0])
        dp = [0] * len(pairs)
        ans = 0
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][0]:
                    dp[i] = max(dp[j], dp[i]+1)
                    ans = max(dp[i], ans)
        return ans

