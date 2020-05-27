import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        banset = set(bank)
        bfs = collections.deque()
        bfs.append((start,0))
        while bfs:
            print(bfs)
            gene, step = bfs.popleft()
            if gene == end: return step
            for i in range(len(gene)):
                for x in 'ACGT':
                    newgene = gene[:i] + x + gene[i+1:]
                    if newgene in banset and newgene != end:
                        bfs.append((newgene,step + 1))
                        banset.remove(newgene)
        return -1

if __name__ == '__main__':
    start="AACCGGTT"
    end="AAACGGTA"
    bank= ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(Solution().minMutation(start,end,bank))