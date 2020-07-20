from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for curDay, curTemp in enumerate(T):
            while stack and curTemp > stack[-1][1]:
                com = stack.pop()
                res[com[0]] = curDay - com[0]
            stack.append([curDay, curTemp])
        return res
print(Solution().dailyTemperatures(
    [73,74,75,71,69,72,76,73]
))