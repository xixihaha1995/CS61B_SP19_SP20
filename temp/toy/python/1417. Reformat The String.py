class Solution:
    def reformat(self, s: str) -> str:
        cha = 0
        num = 0
        for char in s:
            if char >= '0' and char <= '9':
                num += 1
            else:
                cha += 1

        if abs(cha - num) > 1:
            return ""
        if num > cha:
            cha = 1
            num = 0
        else:
            cha = 0
            num = 1
        listone = list(s)
        for char in listone:
            if char >= '0' and char <= '9':
                listone[num] = char
                num += 2
            else:
                listone[cha] = char
                cha += 2
        return ''.join(listone)

print(Solution().reformat("covid2019"))