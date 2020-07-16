class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        store = set()
        for j in J:
            store.add(j)
        res = 0
        for s in S:
            if s in store:
                res += 1

        return res
