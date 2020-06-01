class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.L = []

    def seat(self) -> int:
        N = self.N
        L = self.L
        if not self.L: res = 0
        else:
            d, res = L[0], 0
            for a, b in zip(L, L[1:]):
                if (b-a)/2 > d:
                    d = (b-a)/2
                    res = (b + a)/2
                if N - 1 - L[-1] > d:
                    res = N - 1
        bisect.insort(L, res)
        return res

    def leave(self, p: int) -> None:
        self.L.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)