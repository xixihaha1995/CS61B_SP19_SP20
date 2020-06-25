class DijkStra:
    def __init__(self, start_node, edges:List[Tuple[int,int,int]],nodes:List[int]):

        self.link = {node: {} for node in nodes}
        self.start_node: start_node
        self.S = {start_node:0}
        self.total_nodes_num = len(nodes)

        for a, b, edge_len in edges:
            self.link[a][b] = edge_len
            self.link[b][a] = edge_len
        self.U_que = PriorityQueue()
        for node in nodes:
            if node != start_node:
                if node in self.link[start_node]:
                    self.U_que.put((self.link[start_node][node], node))
                else:
                    self.U_que.put((0x7fffffff, node))
    def getMinPathLen(self):
        while len(self.S) != self.total_nodes_num:
            while True:
                min_edge_len, min_node = self.U_que.get()
                if min_node not in self.S:
                    break
            self.S[min_node] = min_edge_len

            for next in self.link[min_node]:
                if next not in self.S:
                    self.U_que.put((min_edge_len+self.link[min_node][next], next))
        return [(k,v) for k, v in self.S.items()]

class Solution:


    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:

        all_edges = [(a, b, edge_len+1) for a, b, edge_len in edges]
        nodes = [i  for i in range(N)]

        util = DijkStra(0, all_edges, nodes)
        min_path_len = util.getMinPathLen()

        m = {node:[] for node in range(N)}
        help_m = {}
        for a, b,edge_len in edges:
            m[a].append((b,edge_len))
            m[b].append((a, edge_len))
            help_m[(a,b)] = edge_len
            help_m[(b,a)] = edge_len
        visited_nodes = {}

        ans = 0
        for node, path_len in min_path_len:
            if path_len <= M:
                ans += 1
                left_step = M - path_len

                for next, edge_Len in m[node]:
                    visit_cnt = min(edge_len, left_step)
                    if (node, next) not in visited_nodes or visit_cnt < visited_nodes[(node, next)]:
                        visited_nodes[(node, next)] = visit_cnt
        for a in range(N):
            for b in range(a+1, N):
                if (a, b) in help_m:
                    sum = 0
                    if (a,b) in visited_nodes:
                        sum += visited_nodes[(a,b)]
                    if (b,a) in visited_nodes:
                        sum += visited_nodes[(b,a)]
                    ans += min(help_m[(a,b)], sum)
        return ans
