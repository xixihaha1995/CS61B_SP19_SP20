import collections


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        banset = set(bank)
        bfs = collections.deque()
        bfs.append((start,0))
        for i in range(len(gene)):
            while bfs:
                gene, step = bfs.popleft()
                    if gene == end: return i
                    for x in 'ACGT':
                        newgene = gene[:i] + x + gene[i+1:]
                        if newgene in banset and newgene != end:
                            bfs.append(newgene,i+1)
                            banset.remove(newgene)
