from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num

        res = [0,0]
        diff2 = diff
        diff2 &= - diff2
        for num in nums:
            if diff2 & num == 0:
                res[0] ^= num
        res[1] = diff ^ res[0]

        return res



