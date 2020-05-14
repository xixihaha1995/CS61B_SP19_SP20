class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res = false
        self.helper(s, t, res)

    def helper(self, s, t, res):
        return s.__hash__()==t.__hash__() ? True : False


if __name__ == '__main__':
    print(Solution().isAnagram("anagram","nagaram"))