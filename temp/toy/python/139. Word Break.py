from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.m = {}
        return self.helper(s, wordDict)
    def helper(self, s, wordDict):
        if not s: return True
        if s in self.m: return self.m[s]
        if s in wordDict:
            self.m[s] = True
            return True
        for i in range(len(s)+1):
            if s[:i] in wordDict:
                if self.helper(s[i:], wordDict):
                    return True
        self.m[s] = False
        return False

if __name__ == '__main__':
    obj = Solution()
    # s = "catsandog"
    #     # wordDict = ["cats", "dog", "sand", "and", "cat"]
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(obj.wordBreak(s,wordDict))
