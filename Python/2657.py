class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        for i in range(n):
            index = B.index(A[i])
            res[max(i, index)] += 1
        for i in range(1, n):
            res[i] += res[i - 1]
        return res