from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(nums)
        dup = sum(nums) - sum(s)
        check = 0
        for i, num in enumerate(nums, 1):
            temp = i ^ num
            check ^= temp
        dis = check ^dup
        return [dup, dis]

print(Solution().findErrorNums(
    [1,2,2,4]
))