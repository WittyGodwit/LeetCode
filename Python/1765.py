class Solution:
    from collections import deque
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        length = len(isWater)
        width = len(isWater[0])
        height = [[-1] * width for _ in range(length)]
        queue = deque()
        for i in range(length):
            for j in range(width):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append([i, j])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            cell = queue.popleft()
            x, y = cell[0], cell[1]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < length and 0 <= ny < width and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append([nx, ny])
        return height