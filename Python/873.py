class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        n = len(arr)
        maxl = 2
        for i in range(n):
            for j in range(i + 1, n):
                fi1, fi2 = arr[j], arr[i] + arr[j]
                l = 2
                while fi2 in s:
                    fi1, fi2 = fi2, fi1 + fi2
                    l += 1
                maxl = max(maxl, l)
        return maxl if maxl >= 3 else 0