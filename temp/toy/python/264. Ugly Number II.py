class Solution:
    def nthUglyNumber(self, n: int) -> int:
        self.heap = [1]
        self.nums = []
        for _ in range(1690):
            cur = self.heap.pop(0)
            self.nums.append(cur)
            self.heap.append(2 * cur)
            self.heap.append(3 * cur)
            self.heap.append(5 * cur)
        return self.nums[n]
