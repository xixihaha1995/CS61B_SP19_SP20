class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        minsp, maxsp = max(weights), sum(weights)
        while minsp < maxsp:
            mid = int((minsp + maxsp)/2)
            d = 1
            t = 0
            for w in weights:
                t += w
                if t > mid:
                    t = w
                    d += 1
            if d > D: minsp = mid + 1
            else: maxsp = mid
        return minsp