class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s))
        mem = collections.defaultdict(list)
        for l, r in pairs:
            pl = self.find(l)
            pr = self.find(r)
            if pl != pr:
                parent[l] = pr

        for counter, value in enumerate(parent):
            mem[find(value)].append(s[counter])
        for sets in mem:
            mem[set].sorted(reverse = True)
        res = ""
        for i in range(len(s)):
            res.append(mem[find(i)].pop())
        return res

    def find(self, r):
        while parent[r] != r:
            r = parent[r]
        return r


