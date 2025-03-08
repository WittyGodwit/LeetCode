class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = [[0] * (n + 1) for _ in range(3)]
        for i in range(1, 3):
            cost = float("inf")
            for j in range(1, n + 1):
                cost = min(cost, prices[j - 1] - profit[i - 1][j - 1])
                profit[i][j] = max(profit[i][j - 1], prices[j - 1] - cost)
        return profit[-1][-1]