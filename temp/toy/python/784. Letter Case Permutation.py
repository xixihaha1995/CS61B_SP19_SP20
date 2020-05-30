from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.helper(S,res,"")
        return res
    def helper(self, S, res, word):
        if not S:
            res.append(word)
            return
        if S[0].isalpha():
            self.helper(S[1:], res, word + S[0].lower())
            self.helper(S[1:], res, word + S[0].upper())
        else:
            self.helper(S[1:], res, word + S[0])

if __name__ == '__main__':
    print(Solution().letterCasePermutation(
        "a1b2"
    ))
