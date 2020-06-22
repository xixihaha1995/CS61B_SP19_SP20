from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        weight = [0] * 15001
        target = sum(stones) / 2.0
        intTar = int(target)
        for stone in stones:
            for i in range(intTar, stone-1,-1):
                weight[i] = max(weight[i], weight[i-stone] + stone)
        return (target-weight[intTar]) * 2


print(Solution().lastStoneWeightII(
    [2,7,4,1,8,1]
))