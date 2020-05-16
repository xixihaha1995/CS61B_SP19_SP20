class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = []
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
        return dp[len(cost)-1]


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs( [10, 15, 20]))
