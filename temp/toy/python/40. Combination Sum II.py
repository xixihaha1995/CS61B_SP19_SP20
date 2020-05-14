class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(candidates, res, target, 0, [])
        return res

    def helper(self, candidates, res, remainder, index, path):
        if (remainder < 0):
            return
        if (remainder == 0):
            res.append(path[:])
        for i in range(index, len(candidates)):
            path.append(candidates[i])
            self.helper(candidates, res, remainder - candidates[i], i+1, path)
            path.pop()
            # temp.pop()


if __name__ == '__main__':
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
