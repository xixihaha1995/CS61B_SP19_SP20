class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = dict()
        window = dict()
        for chara in p:
            if chara in need:
                need[chara] += 1
            else:need[chara] = 1
        left, right = 0, 0
        valid = 0
        res = []
        while right < len(s):
            curChar = s[right]
            right += 1
            # exploration
            if curChar in need:
                if curChar in window:
                    window[curChar] += 1
                else: window[curChar] = 1
                if window[curChar] == need[curChar]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                deleChar = s[left]
                left += 1
                if deleChar in need:
                    if window[deleChar] == need[deleChar]:
                        valid -= 1
                    window[deleChar] -= 1
        return res




