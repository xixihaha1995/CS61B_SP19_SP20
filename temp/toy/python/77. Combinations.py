from xlwt.compat import xrange


class Solution(object):

    def __init__(self):
        self.res =[]
        self.helper(range( 1, n+1), k, self.res, [])

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """


        def helper(array, k, res, path):
            if k > len(array):
                return
            if k == 0:
                self.res.append(path)
            else:
                for i in array:
                    self.helper(array[i+1:], k - 1, res, path + [array[i]])


if __name__ == '__main__':
    print(Solution().combine(4,2))