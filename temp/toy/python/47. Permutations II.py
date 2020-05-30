from xlwt.compat import xrange


class Solution(object):

    def __init__(self):
        self.res = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        visited = [False] * n
        res = []
        self.helper(nums, res, visited, [],0)
        return res
    def helper(self, nums, res, visited, path, count):
        if len(nums) == count:
            res.append(path[:])
            return
        for i in range(len(nums)):
            if visited[i]: continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]: continue
            visited[i] = True
            path.append(nums[i])
            self.helper(nums, res, visited, path, count + 1)
            path.pop()
            visited[i] = False



if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
