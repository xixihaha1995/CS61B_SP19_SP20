from numpy import long


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        self.helper(num, target, result, "", 0, 0, 0)
    def helper(self, num, target, result, path, start, eval, pre ):
        if start == len(num):
            if target == eval:
                result.append(path)
            return
        for i in range(start, len(num)):
            if num[start] == '0' and i > start: break
            cur = int(path[start: i+1])
            lenth = len(path)
            if start == 0:
                self.helper(num, target, result, path+str(cur), i+1, cur, cur)
                path = path[:lenth]
            else:
                self.helper(num, target, result, path + "+" + str(cur), i+1, eval + cur, cur)
                path = path[:lenth]

                self.helper(num, target, result, path + "-" + str(cur), i+1, eval -cur, -cur)
                path = path[:lenth]

                self.helper(num, target, result, path + "*"+ str(cur), i+1, eval -pre + pre * cur, pre * cur)
                path = path[:lenth]