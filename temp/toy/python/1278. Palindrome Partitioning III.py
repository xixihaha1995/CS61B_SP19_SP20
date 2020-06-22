from functools import lru_cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @lru_cache(None)
        def check(l, r):
            res = 0
            while l <= r:
                if s[l] != s[r]:
                    res += 1
                l += 1
                r -= 1
            return res

        @lru_cache(None)
        def dfs(l,r,t):
            if (t==1):
                return check(l,r)
            res = float('inf')
            for i in range(0,r):
                res= min(res, dfs(0, i, t-1)+check(i+1,r))
            return res

        return dfs(0, len(s) - 1, k)

print(Solution().palindromePartition(
    "abc", 2
))