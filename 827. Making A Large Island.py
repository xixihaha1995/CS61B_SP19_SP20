class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j, grid, newnumber):

