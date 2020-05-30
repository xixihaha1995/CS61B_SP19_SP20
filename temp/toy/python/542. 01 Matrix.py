class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:return matrix
        m, n = len(matrix), len(matrix[0])
        res = matrix[:]
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append([[i,j],0])
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        visited = [[0]*(n+1)]*(m+1)
        while q:
            tmp, distance = q.popleft()
            x0,y0 = tmp[0], tmp[1]

            if matrix[x0][y0] == 1:
                res[x0][y0] = distance
            for k in range(4):
                x = x0+dx[k]
                y = y0+dy[k]

                if 0<= x< m and 0<= y<n and visited[x][y] != 1:
                    q.append([[x,y], distance + 1])
                    visited[x][y] = 1
        return res

