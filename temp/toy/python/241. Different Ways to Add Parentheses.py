from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        N = len(input)
        for i in range(N):
            if input[i] in "+-*":
                lefts = self.diffWaysToCompute(input[:i])
                rights = self.diffWaysToCompute(input[i+1:])
                for left in lefts:
                    for right in rights:
                        if input[i] == '+':
                            res.append(left + right)
                        elif input[i] == '-':
                            res.append(left - right)
                        elif input[i] == '*':
                            res.append(left * right)
        if not res: res.append(int(input))
        return res

if __name__ == '__main__':
    print(Solution().diffWaysToCompute(
        "2-1-1"
    ))
