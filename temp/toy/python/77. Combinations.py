from xlwt.compat import xrange


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper  = (range( 1, n+1), k, path)

        def helper(array, k, path):
            if k > len(array):
                return
            if k == 0:
                return
            else
                for i in array:
                    self.helper(array[i+1:], k - 1, path + array[i])


if __name__ == '__main__':
    print(Solution().combine(4,2))