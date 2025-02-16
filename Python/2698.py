class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(num: int, target: int) -> bool:
            if num == 0:
                return target == 0
            if num == target:
                return True
            m = 1
            while num >= m:
                m *= 10
                if partition(num // m, target - num % m):
                    return True
        return sum(i * i for i in range(1, n + 1) if partition(i * i, i))