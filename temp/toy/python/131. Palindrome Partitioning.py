class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.isPalindrome = lambda s : s == s[::-1]
        res = []
        self.helper(s, res, [])
        return res

    def helper(self, s, res,  path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                path.append(s[:i])
                self.helper(s[i:],res, path )
                path.pop()


if __name__ == '__main__':
    print(Solution().partition( "aab"))