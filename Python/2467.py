class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        res = float("-inf")
        n = len(amount)
        self.visited = [False] * n
        self.adj = [[] for _ in range(n)]
        self.path = {}
        for edge in edges:
            self.adj[edge[0]].append(edge[1])
            self.adj[edge[1]].append(edge[0])
        self.dfs(bob, 0)
        self.visited = [False] * n
        queue = deque([[0, 0, 0]])
        while queue:
            node, time, income = queue.popleft()
            if node not in self.path or time < self.path[node]:
                income += amount[node]
            elif self.path[node] == time:
                income += amount[node] / 2
            if len(self.adj[node]) == 1 and node != 0:
                res = max(res, income)
            for a in self.adj[node]:
                if not self.visited[a]:
                    queue.append([a, time + 1, income])
            self.visited[node] = True
        return int(res)

    def dfs(self, node: int, time: int) -> bool:
        self.path[node] = time
        self.visited[node] = True
        if node == 0:
            return True
        for a in self.adj[node]:
            if not self.visited[a] and self.dfs(a, time + 1):
                return True
        del self.path[node]
        return False