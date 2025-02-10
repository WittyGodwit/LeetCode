class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        def moves(row: int, col: int) -> int:
            if (row, col) in memo:
                return memo[(row, col)]
            if col + 1 >= n:
                return 0
            step = 0
            for row_move in (-1, 0 ,1):
                new_row, new_col = row + row_move, col + 1
                if 0 <= new_row < m and 0<= new_col < n and grid[new_row][new_col] > grid[row][col]:
                    step = max(step, 1 + moves(new_row, new_col))
            memo[(row, col)] = step
            return step
        max_step = 0
        for i in range(m):
            max_step = max(max_step, moves(i, 0))
        return max_step