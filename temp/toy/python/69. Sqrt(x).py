class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = int((right+left)/2)
            if mid*mid > x:
                right = mid -1
            else:left = mid + 1
        return right

if __name__ == '__main__':
    print(Solution().mySqrt(8))