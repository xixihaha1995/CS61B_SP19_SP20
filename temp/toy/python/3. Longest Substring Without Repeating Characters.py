class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        n = len(s)
        curlen = 0
        maxlen = 0
        lookup = set()
        for i in range(n):
            curlen  += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                curlen -= 1
            lookup.add(s[i])
            if curlen > maxlen: maxlen  = curlen

        return maxlen