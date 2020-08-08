class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, muli = [], "", 0
        for cha in s:
            if cha == '[':
                stack.append([muli,res])
                res, muli = "", 0
            elif cha == ']':
                curMuli, lastRes = stack.pop()
                res = lastRes + curMuli * res
            elif '0' <= cha <= '9':
                muli = muli * 10 + int(cha)
            else:
                res += cha
        return res
