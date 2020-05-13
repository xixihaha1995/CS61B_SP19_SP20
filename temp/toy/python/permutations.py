from xlwt.compat import xrange


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(nums, temp):
            if len(nums) == len(temp):
                self.res.append(temp[:])
                return
            for i in xrange(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(nums, temp)
                temp.pop()

        dfs(nums, [])
        return self.res


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
