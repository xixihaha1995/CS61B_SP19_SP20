from functools import lru_cache
from typing import List


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        @lru_cache(None)
        def dp(i,j):
            return 0 if j -i <= 1 else min(dp(i,k) + dp(k,j) + A[i] *A[k] *A[j] for k in range(i+1,j))

        return dp(0, len(A) -1)

print(Solution().minScoreTriangulation(
    [1,3,1,4,1,5]
))