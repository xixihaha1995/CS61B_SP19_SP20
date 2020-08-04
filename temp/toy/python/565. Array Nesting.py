from collections import Set


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            count = 0
            k = i
            while nums[k] != -1:
                temp = k
                k = nums[k]
                nums[temp] = -1
                count += 1
            res = max(res, count)
        return res

