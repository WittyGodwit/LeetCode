class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        position = {}
        for i in range(row):
            for j in range(col):
                position[mat[i][j]] = [i, j]
        nrow = [0] * row
        ncol = [0] * col
        for a in arr:
            r, c = position[a][0], position[a][1]
            nrow[r] += 1
            ncol[c] += 1
            if nrow[r] == col or ncol[c] == row:
                return arr.index(a)