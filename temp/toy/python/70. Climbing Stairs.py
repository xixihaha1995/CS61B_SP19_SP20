class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        prev = 1
        prevprev = 1
        self.res = 0
        for i in range(1,n):
            self.res = prev + prevprev
            prevprev = prev
            prev = self.res
        return self.res


if __name__ == '__main__':
    print(Solution().climbStairs(4))
