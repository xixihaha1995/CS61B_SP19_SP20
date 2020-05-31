class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        res = []
        self.dfs(S, res, [])
        return res

    def dfs(self, str, res, path):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]: return False
        if not str and len(path) >= 3:
            res.extend(path)
            return True

        for i in range(len(str)):
            curr = str[:i + 1]
            if (curr[0] == '0' and len(curr) != 1) or int(curr) >= 2 ** 31: continue
            if self.dfs(str[i + 1:], res, path + [int(curr)]): return True
        return False
