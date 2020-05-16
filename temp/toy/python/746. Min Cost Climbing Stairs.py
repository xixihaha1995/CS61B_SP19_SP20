class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        res = 0
        for i in range(2,len(cost)):
            res = res + min(cost[i-1],cost[i-2])
        return res


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs( [10, 15, 20]))
