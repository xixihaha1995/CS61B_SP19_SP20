from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        kincost = 1e9
        cost = [kincost] * n
        cost[src] = 0
        for i in range(K+1):
            temp = list(cost)
            for flight in flights:
                temp[flight[1]] = min(cost[flight[0]] + flight[2], temp[flight[1]] )
            cost = temp
        return -1 if cost[dst] >=1e9 else cost[dst]


if __name__ == '__main__':
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(Solution().findCheapestPrice(
        n,edges,src,dst,k

    ))
