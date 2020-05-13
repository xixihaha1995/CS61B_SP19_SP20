from xlwt.compat import xrange


class Solution(object):
    def __init__(self):
        self.res = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, temp, index):
            self.res.append(temp[:])

            for i in xrange(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])

                dfs(nums, temp, i+1)
                temp.pop()

        dfs(nums, [], 0)
        return self.res


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))
