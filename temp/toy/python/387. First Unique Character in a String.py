class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = dict()
        for char in s:
            if char in table:
                table[char] += 1
            else:table[char] = 1
        for i in range(len(s)):
            if table[s[i]] == 1:
                return i
        return -1
