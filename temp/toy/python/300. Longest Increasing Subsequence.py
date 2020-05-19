from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lencur = 1
        n = len(nums)
        cur = nums[0]
        for i in range(1,n):
            if nums[i] < nums[i - 1] and lencur == 1:
                cur = nums[i]
            if nums[i] > cur:
                cur = nums[i]
                lencur += 1
        return lencur


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
