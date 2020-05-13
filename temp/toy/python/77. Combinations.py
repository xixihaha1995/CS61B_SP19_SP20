from xlwt.compat import xrange


class Solution(object):
    def __init__(self):
        self.res = []
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(nums, temp, count):
            if count == 1:
                self.res.append(temp)
                return

            for i in nums:
                if i in temp:
                    continue
                temp.append(i)
                nums.remove(i)
                dfs(nums, temp, count - 1)

        nums = []
        for i in xrange(1,n+1):
            nums.append(i)
        dfs(nums, [], k)
        return self.res



if __name__ == '__main__':
    print(Solution().combine(4,2))