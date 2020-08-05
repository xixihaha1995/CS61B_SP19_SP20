from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        idx = -1
        res = [[] for _ in range(len(intervals))]
        for interval in intervals:
            if idx == -1 or res[idx][1] < interval[0]:
                idx += 1
                res[idx] = interval
            else:
                res[idx][1] = max(res[idx][1], interval[1])

        return res
