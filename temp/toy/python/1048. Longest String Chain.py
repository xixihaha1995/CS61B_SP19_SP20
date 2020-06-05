import functools
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words: return 0

        def mycmp(x, y):
            return len(x) - len(y)
        words.sort(key=functools.cmp_to_key(mycmp))

        n = len(words)
        dp = [1] * n
        longest = 1
        for i in range(0, n):
            for j in range(i):
                if self.diffone(words[i], words[j]):
                    dp[i] = dp[j] + 1
                    # print(dp[i])
                    longest = max(longest, dp[i])
        return longest

    def diffone(self, stra, strb):
        if len(stra) != len(strb) + 1: return False
        i, j = 0, 0
        count = 0
        while i < len(stra) and j < len(strb):
            if stra[i] == strb[j]:
                i += 1
                j += 1
            else:
                count += 1
                i += 1
        return count <= 1


if __name__ == '__main__':
    print(
        Solution().longestStrChain(
            # ["sgtnz", "sgtz", "sgz", "ikrcyoglz", "ajelpkpx", "ajelpkpxm", "srqgtnz", "srqgotnz", "srgtnz",
            #  "ijkrcyoglz"]
            # ["a", "b", "ba", "bca", "bda", "bdca"]
            ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj",
             "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]
        )
    )
