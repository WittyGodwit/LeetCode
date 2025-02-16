class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapq.heapify(nums)
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y if x <= y else y * 2 + x)
            res += 1
        return res