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
            for i xrange(len(nums)):
                if (i in temp):
                    continue
                temp.append(nums[i])
                dfs(nums,temp)
                temp.pop()
        dfs(nums,[])
        return self.res