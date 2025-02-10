class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True
        for j in range(len(nums) - 1):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1] and bin(nums[i]).count('1') == bin(nums[i + 1]).count('1'):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums == sorted(nums)