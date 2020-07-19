class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s)) ] for _ in range(len(s))]
        ans = 0
        for i in range(len(s)):
            dp[i][i] =True
        for right in range(len(s)):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left < 3 or dp[left+1][right-1]):
                    dp[left][right] = True
                    ans += 1
        return ans
        # ans = [0] * len(s)
        # for right in range(len(s)):
        #     for left in range(right + 1):
        #         if dp[left][right]:
        #             ans[right] += 1
        # return sum(ans)
