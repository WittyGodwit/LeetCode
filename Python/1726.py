class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        import math
        n = len(nums)
        freq = {}
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                freq[product] = freq.get(product, 0) + 1
        return sum(8 * (f * (f - 1) // 2) for f in freq.values() if f > 1)