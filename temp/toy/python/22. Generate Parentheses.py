from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, n, n, "")
        return res

    def helper(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.helper(res, left - 1, right, path + "(")
        if left < right:
            self.helper(res, left, right - 1, path + ")")


if __name__ == '__main__':
    print(Solution().generateParenthesis( 3 ))