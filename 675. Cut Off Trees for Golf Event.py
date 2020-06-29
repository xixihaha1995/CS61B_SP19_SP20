class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def dist(forest, sr, sc, tr, tc):
            R, C = len(forest), len(forest[0])
            heap = [(0, 0, sr, sc)]
            cost = {(sr. sc): 0}

            while heap:
                f, g, r, c = heapq.heappop(heap)
                if r == tc and c = tc: return g

                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                        ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                        if ncost < cost.get((nr, nc), 9999):
                            cost[nr, nc] = ncost
                            heapq.heappush(heap, (ncost, g+1, nr, nc))
            return -1


        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for _, tr, tc in trees:
            d = dist(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans
