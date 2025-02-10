class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        nrow = [sum(grid[i]) for i in range(row)]
        ncolumn = [sum(grid[i][j] for i in range(row)) for j in range(column)]
        res = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    if nrow[i] >= 2:
                        res += 1
                    elif ncolumn[j] >= 2:
                        res += 1
        return res