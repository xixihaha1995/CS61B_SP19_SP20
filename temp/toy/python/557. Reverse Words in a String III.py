class Solution:
    def reverseWords(self, s: str) -> str:
        reWord = lambda x:x[::-1]
        res  = []
        data = list(s.split())
        for word in data:
            res.append(reWord(word))
        return " ".join(res)