class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2: return n

        points.sort(key=lambda x: x[1])

        end = points[0][1]
        res = 1
        for i in range(1, n):
            if points[i][0] > end:
                res += 1
                end = points[i][1]
        return res