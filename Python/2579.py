class Solution:
    def coloredCells(self, n: int) -> int:
        color = 1
        while n - 1:
            color += 4 * (n - 1)
            n -= 1
        return color