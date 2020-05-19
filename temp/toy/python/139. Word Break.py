from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        print(s)
        print(wordDict)
        dp = [False] * (len(s) +1)
        dp[0] = True
        for i in range(1,len(s) +1):
            for k in range(0,i):
                if dp[i-1] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[-1]

if __name__ == '__main__':
    obj = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(obj.wordBreak(s,wordDict))
