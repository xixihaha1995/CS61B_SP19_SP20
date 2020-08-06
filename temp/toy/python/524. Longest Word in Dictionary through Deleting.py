class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        ans, anslen = "", 0
        for dStr in d:
            i, j =0
            while i < len(s) and j < len(dStr):
                if s[i] == dStr[j]:
                    i += 1
                    j += 1
                else: i += 1
                if j == len(dStr):
                    if j > len(dStr) or ( j== len(dStr) and dStr < ans):
                        ans = dStr
                        anslen = j
        return ans

