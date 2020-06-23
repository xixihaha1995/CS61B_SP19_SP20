import collections
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        count = collections.defaultdict(list)
        for cl in clips:
            if cl[0] in count:
                if cl[1] - cl[0] > count[cl[0]][1] - count[cl[0]][0]:
                    count[cl[0]].pop()
                    count[cl[0]] = cl
            else:
                count[cl[0]] = cl

        if 0 not in count: return -1
        prev = 0
        cur = count[0][1]
        next = cur
        res = 1
        while cur < T:
            hasFind = False
            for c in range(cur, prev, -1):
                if c in count:
                    if count[c][1] > next:
                        next = count[c][1]
                        prev = c
                        hasFind = True
            if not hasFind: return -1
            cur = next
            res += 1
        return res

print(Solution().videoStitching(
    [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10
))