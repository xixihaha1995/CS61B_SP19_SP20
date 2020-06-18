class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(set(s))== 1: return s
        start, end, maxL = 0, 0, 0
        n = len(s)
        dp = [[0]* n for _ in range(n)]
        for i in range(len(s)):
            for j in range(i):
                dp[j][i] = (s[i] == s[j]) and (dp[j+1][i-1] or i - j < 2)
                if dp[j][i] and maxL < i -j + 1:
                    maxL = i-j + 1
                    start = j
                    end = i
            dp[j][i] = 1
        return s[start:end+1]

