class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for curDay, curTemp in enumerate(T):
            if curTemp > stack[-1][1]:
                com = stack.pop()
                res[com[0]] = curDay - com[1]
            else:
                stack.append((curDay, curTemp))
        return res
