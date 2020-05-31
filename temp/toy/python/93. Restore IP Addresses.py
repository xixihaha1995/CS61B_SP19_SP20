class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        res = []
        self.dfs(s, [], res)
        return res
    def dfs(self, s, path, res):
        if not s and len(path) == 4:
            res.append(".".join(path))
            return
        for i in range(1,4):
            if len(s)< i: continue
            number = int(s[:i])
            if number <= 255:
                self.dfs(s[i:], path + [s[:i]], res)