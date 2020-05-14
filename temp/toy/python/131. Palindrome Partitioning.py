class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.isPalindrome = lambda s : s == s[::-1]
        res = []
        self.helper(s, res, 0, [])
        return res
    def helper(self, s, res, index, path):
        if not s:
            res.append(path)
        for i in range(1, len(s) + 1):
            if isPalindrome(s[:i]):
                self.helper(s[i:],res, i + 1, path + [s[:i]])

