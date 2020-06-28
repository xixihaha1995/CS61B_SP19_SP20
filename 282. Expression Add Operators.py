from numpy import long


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        self.helper(num, target, result, [], 0, 0, 0)
    def helper(self, num, target, result, path, start, eval, pre ):
        if start == len(num):
            if target == eval:
                result.append(str(path))
            return
        for i in range(start, len(num)):
            if num[start] == '0' and i > start: break
            cur = long(float(path[start: i+1]))
            len = len(path)
            if start == 0:
                self.helper(num, target, result, path.append(cur), i+1, cur, cur)
                path = path[:len]
            else:
                self.helper(num, target, result, path.append("+").append(cur), i+1, eval + cur, cur)
                path = path[:len]

                self.helper(num, target, result, path.append("-").append(cur), i+1, eval -cur, -cur)
                path = path[:len]

                self.helper(num, target, result, path.append("*").append(cur), i+1, eval -pre + pre * cur, pre * cur)
                path = path[:len]

