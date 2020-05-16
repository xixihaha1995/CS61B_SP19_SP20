class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        for index in range(i, j+1):
            res = res + self.nums[i]
        return res

if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    param_1 = obj.sumRange(0, 5)
    print(param_1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)