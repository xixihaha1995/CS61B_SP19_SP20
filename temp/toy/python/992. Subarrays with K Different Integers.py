class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        table = {}
        ans= 0
        count = 0
        for (right =0; right <len(A); right++):
            table[A[right]]+=1