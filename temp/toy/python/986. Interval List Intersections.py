class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            s = max(A[i].start, B[j].start)
            e = min(A[i].end, B[j].end)
            if s<=e: res.append([s,e])
            if A[i].end < B[j].end: i += 1
            else: j += 1
        return res