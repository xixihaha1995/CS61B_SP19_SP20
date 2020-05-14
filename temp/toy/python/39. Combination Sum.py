class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(candidates, res, target, 0, [])
        return res

    def helper(self, candidates, res, target, index, path):
        if (target < 0):
            return
        if (target == 0):
            res.append(path)
        for i in range(index, len(candidates)):
            path.append(candidates[i])
            self.helper(candidates, res, target - candidates[i], i, path)
            path.pop()
            # temp.pop()


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
