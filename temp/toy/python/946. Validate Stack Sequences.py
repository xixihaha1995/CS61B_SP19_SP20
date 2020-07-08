from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [None] * len(pushed)
        size, j = 0, 0
        for i in range(len(pushed)):
            stack[size] = pushed[i]
            size += 1
            while size != 0 and stack[size - 1] == popped[j]:
                size -= 1
                j += 1
        return size == 0
print(Solution().validateStackSequences(
    [1,2,3,4,5], [4,5,3,2,1]
))
