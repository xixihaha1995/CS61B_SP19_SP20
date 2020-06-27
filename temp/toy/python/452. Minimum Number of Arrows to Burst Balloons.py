class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2: return n

        points.sort(key = lambda x:x[1])

        end = points[0][1]
        res = 1
        for point in points:
            if point[0] > end:
                res += 1
                end = min(end, point[1])
        return res