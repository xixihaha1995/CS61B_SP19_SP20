class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(':')', '[':']','{':'}'}
        stack = ['?']
        for par in s:
            if par in match: stack.append(par)
            elif match[stack.pop()] != c: return False
        return True
