class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = {}
        for x in xrange(arr):
            if x - difference in res:
                res.append(x)
            else:
                break
        return len(res)

