class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dictUpdate = {}
        dp = [0] *  (max(num) + 1)
        for idx, value in enumerate(nums):
            dictUpdate[value] = idx
            dp[value] += 1
        degree = max(dp)
        res = 0
        for i in range(len(dp)):
            if dp[i] == degree:
                end = dictUpdate[i]
                start = nums.index(i)
                res = min(res, end - start + 1)
        return res

