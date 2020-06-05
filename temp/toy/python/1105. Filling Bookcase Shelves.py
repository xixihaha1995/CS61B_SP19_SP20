class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        n = len(books)
        dp = [float('inf')] * n
        for i in range(n):
            w = 0
            h = 0
            for j in range(i, n):
                w += books[j][0]
                if w > shelf_width: break
                h = max(h, books[j][1])
                dp[j] = min(dp[j], (0 if i == 0 else dp[i - 1] )+ h)
        return max(dp)


if __name__ == '__main__':
    books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]];
    shelf_width = 4
    print(
        Solution().minHeightShelves(
            books, shelf_width

        )
    )