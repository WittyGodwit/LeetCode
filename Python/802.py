class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(index: int, visit: List[int]) -> bool:
            if visit[index] >= 0:
                return visit[index]
            visit[index] = 0
            for node in graph[index]:
                if not dfs(node, visit):
                    return False
            visit[index] = 1
            return True

        n = len(graph)
        visit = [-1] * n
        safe = []

        for i in range(n):
            if dfs(i, visit):
                safe.append(i)
        return safe