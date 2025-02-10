class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        sum0, sum1 = [0] * col, [0] * col
        sum0[0], sum1[0] = grid[0][0], grid[1][0]
        for i in range(1, col):
            sum0[i] = sum0[i - 1] + grid[0][i]
            sum1[i] = sum1[i - 1] + grid[1][i]
        value = [0] * col
        m = sum0[col - 1] - sum0[0]
        for i in range(1, col):
            m = min(m, max(sum0[col - 1] - sum0[i], sum1[i - 1]))
        return m