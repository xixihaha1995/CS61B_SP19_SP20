class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortns = []
        res = []
        for n in reversed(nums):
            idx = bisect.bisect_left(sortns,n)
            res.append(idx)
            sortns.insert(idx, n)
        return res[::-1]