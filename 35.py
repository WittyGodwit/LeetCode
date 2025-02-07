class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for num in nums:
            if num == target:
                return nums.index(num)
result = [1, 3, 5, 6]
target = 5
sol = Solution().searchInsert(result, target)
print(sol)
