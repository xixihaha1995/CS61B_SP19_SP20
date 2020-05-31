class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        minsp, maxsp = 1, sum(piles)
        while minsp < maxsp:
            mid = int((minsp + maxsp)/2)
            curh = 0
            for pile in piles:
                curh += pile//k + (1 if pile % k else 0)
            if curh > H: minsp = mid
            else: maxsp = mid -1
        return minsp
