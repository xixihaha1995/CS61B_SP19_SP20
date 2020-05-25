import collections
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))
        def find(r):
            if parent[r] != r:
                parent[r] = find(parent[r])
            return r

        for l, r in pairs:
            pl = find(l)
            pr = find(r)
            if pl != pr:
                parent[pl] = pr

        mem = collections.defaultdict(list)
        for counter, value in enumerate(parent):
            mem[find(value)].append(s[counter])
        for sets in mem:
            mem[sets].sort(reverse = True)
        res = []
        for i in range(len(s)):
            res.append(mem[find(i)].pop())
        return "".join(res)


if __name__ == '__main__':
    s = "dcab"
    pairs = [[0, 3], [1, 2]]
    print(Solution().smallestStringWithSwaps(s, pairs))



