class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost)+1)
        cost.append(0)

        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1],dp[i-2])+ cost[i]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs(  [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
