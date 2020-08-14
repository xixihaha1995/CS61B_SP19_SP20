from heapq import heappush, heappop


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        self.heap = [1]
        self.nums = []
        self.seen = {1}
        for _ in range(1690):
            cur = heappop(self.heap)
            self.nums.append(cur)
            for k in(2, 3, 5):
                if cur * k not in self.seen:
                    heappush(self.heap, cur * k)
                    self.seen.add(cur*k)
        return self.nums[n-1]

print(Solution().nthUglyNumber(10))
