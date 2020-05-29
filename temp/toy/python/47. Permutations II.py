from xlwt.compat import xrange


class Solution(object):

    def __init__(self):
        self.res = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, res,[])
        return res
    def helper(self, nums, res, path):
        if not nums and path not in res:
            res.append(path[:])
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1], res, path +[nums[i]])
        self.helper()


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
