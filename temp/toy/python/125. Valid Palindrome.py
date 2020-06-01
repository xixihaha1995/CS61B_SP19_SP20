class Solution:
    def isPalindrome(self, s: str) -> bool:
        isValid = lambda x: x==x[::-1]
        str = ''.join([x for x in s.lower() if x.isalnum()])
        return isValid(str)