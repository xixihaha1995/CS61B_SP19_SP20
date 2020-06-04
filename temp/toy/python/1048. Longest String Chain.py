from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words: return 0
        words.sort()
        n = len(words)
        dp = [1] * n
        longest = 1
        for i in range(1,n):
            for j in range(i):
                if len(words[i]) == len(words[j]) + 1:
                    for char in words[j]:
                        if char not in words[i]:
                            continue
                    dp[i] = dp[j] + 1
                    longest = max(longest, dp[i])
        return longest


if __name__ == '__main__':
    print(
        Solution().longestStrChain(
            ["a", "b", "ba", "bca", "bda", "bdca"]
        )
    )