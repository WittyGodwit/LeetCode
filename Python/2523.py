class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right <= 2:
            return [-1, -1]
        integers = [0 if i % 2 == 0 else 1 for i in range(right + 1)]
        integers[1], integers[2] = 0, 1
        for i in range(2, int(right ** 0.5) + 1):
            if integers[i]:
                for j in range(i * i, right + 1, i):
                    integers[j] = 0
                integers[i] = 1
        pairs = [i for i in range(right + 1) if integers[i] == 1 and left <= i <= right]
        if len(pairs) < 2:
            return [-1, -1]
        minimum = float("inf")
        res = []
        for i in range(len(pairs) - 1):
            diff = pairs[i + 1] - pairs[i]
            if diff < minimum:
                res = [pairs[i], pairs[i + 1]]
                minimum = diff
        return res