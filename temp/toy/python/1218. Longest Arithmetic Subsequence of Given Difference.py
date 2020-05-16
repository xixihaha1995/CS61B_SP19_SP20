from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = {}
        for num in arr :
            res[num] = res[num-difference] + 1 if num - difference in res else 1
        return max(res.values())

if __name__ == '__main__':
    print(Solution().longestSubsequence([1,5,7,8,5,3,4,2,1], -2))


