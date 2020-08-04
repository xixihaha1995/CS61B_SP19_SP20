from collections import Set


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        setres = Set()
        res = 0
        for i in range(len(nums)-1):
            count = 0
            k = i
            while nums[k] not in setres:
                setres.add(nums[k])
                count += 1
                k = nums[k]
            res = max(res, count)
        return res

