class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = 0
        f2 = 0
        mincost =
        for i in range(len(cost))
            mincost =  cost[i] + min(f1, f2)
            f1= f2
            f2 = mincost
        return min(f1, f2)

if __name__ == '__main__':
    print(Solution().minCostClimbingStairs(  [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
