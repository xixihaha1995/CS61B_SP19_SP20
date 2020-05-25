class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)
    def dfs(self, rooms, cur, visited):
        if cur in visited: return
        visited.add(cur)
        for key in rooms[cur]:
            self.dfs(rooms, key, visited)