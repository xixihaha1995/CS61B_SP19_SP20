from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.res = 0
        self.dp(sorted(coins), amount)
        return self.res

    def dp(self, coins, remainder):
        if remainder < 0:
            self.res = -1
            return self.res
        if remainder == 0:
            return self.res
        for i in range(len(coins)-1,-1,-1):
            # print(coins[i])
            if coins[i] <= remainder:
                self.res += 1
                self.dp(coins, remainder-coins[i])
                break

if __name__ == '__main__':
    print(Solution().coinChange(
        [1, 2, 5], 11
    ))
