import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        item = []
        for ele in matrix:
            item.extend(ele)
        heapq.heapify(item)
        for i in range(k):
            res = item.pop()
        return res
