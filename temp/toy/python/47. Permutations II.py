from xlwt.compat import xrange


class Solution(object):

    def __init__(self):
        self.res = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, temp, index):
            if len(nums) == len(temp):
                self.res.append(temp[:])
                return
            for i in xrange(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                dfs(nums, temp, i + 1)
                temp.pop()

        dfs(nums, [], 0)
        return self.res


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
