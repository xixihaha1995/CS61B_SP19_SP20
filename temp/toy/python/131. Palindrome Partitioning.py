from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        isvalid = lambda x: x == x[::-1]
        res = []
        path = []
        def helper(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1,len(s)+1):
                if isvalid(s[:i]):
                    path.append(s[:i])
                    helper(s[i:], path, res)
                    path.pop()
        helper(s, path, res)
        return res


if __name__ == '__main__':
    print(Solution().partition( "aab"))