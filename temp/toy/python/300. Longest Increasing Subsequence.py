import collections
import copy
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = collections.defaultdict(set)
        longest = 1
        for i in range(len(nums)):
            dp[nums[i]].add(nums[i])
            for j in range(i):
                if nums[i] > nums[j] and len(dp[nums[i]]) <= len(dp[nums[j]]):
                    dp[nums[i]] = copy.deepcopy(dp[nums[j]])
                    dp[nums[i]].add(nums[i])
                    print(dp[nums[i]])
                    longest = max(longest, len(dp[nums[i]]))
        return longest


if __name__ == '__main__':
    # print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]))
