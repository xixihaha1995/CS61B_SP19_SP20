class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(candidates, temp, target, index)
        return res

    def helper(self, candidates, temp, target, index):
        if (target < 0):
            return
        if (target == 0):
            res.append(temp)
        for i in range (index, len(candidates)):
            temp.append(candidates[i])
            self.helper(candidates,temp,target-candidates[i],i)
            temp.pop()