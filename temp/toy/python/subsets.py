from xlwt.compat import xrange


class Solution(object):
    def __init__(self):
        self.res = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, temp, index):
            self.res.append(temp[:])

            for i in xrange(i, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i)
                temp.pop()

        dfs(nums, [], 0)
        return self.res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
