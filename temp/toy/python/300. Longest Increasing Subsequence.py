import collections
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = collections.defaultdict(list)
        longest = []
        for i in range(len(nums)):
            dp[nums[i]].append(nums[i])
            for j in range(i):
                if nums[i] > nums[j] and len(dp[nums[i]]) <= len(dp[nums[j]]):
                    dp[nums[i]] = dp[nums[j]][:]
                    dp[nums[i]].append(nums[i])
                    if len(dp[nums[i]]) > len(longest):
                        longest = dp[nums[i]][:]
        return len(longest)


if __name__ == '__main__':
    # print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
