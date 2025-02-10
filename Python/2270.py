class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        sums = [0] * len(nums)
        res = 0
        for i in range(1, len(nums)):
            sums[i] = sums[i - 1] + nums[i - 1]
            if sums[i] >= s - sums[i]:
                res += 1
        return res