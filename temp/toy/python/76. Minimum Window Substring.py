class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        minlen = float('inf')
        counter = len(t)
        res = ""

        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1

            lookup[s[end]] -= 1
            end += 1
            # counter是用来干嘛的
            while counter == 0:
                if minlen > end - start:
                    minlen = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    print(Solution().minWindow(
        S, T
    ))