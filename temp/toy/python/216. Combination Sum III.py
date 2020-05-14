class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(range(1, 9), res, k, n, 0, [])
        return res

    def helper(self, nums, res, count, remainder, index, path):
        if (remainder < 0):
            return
        if (count == 0 and remainder == 0):
            res.append(path[:])
        for i in range(index, len(nums)):

            self.helper(nums, res, count - 1, remainder - nums[i], i+1, path + [nums[i]])


if __name__ == '__main__':
    print(Solution().combinationSum3(3, 7))
