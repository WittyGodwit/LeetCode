class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]
        d = 0
        dollar = [0] * (n + 1)
        for i in range(1, n + 1):
            if i in days:
                one = dollar[i - 1] + costs[0]
                seven = dollar[i - 7] + costs[1] if i >= 7 else costs[1]
                thirty = dollar[i - 30] + costs[2] if i >= 30 else costs[2]
                dollar[i] = min(one, seven, thirty)
                d += 1
            else:
                dollar[i] = dollar[i - 1]
        return dollar[n]