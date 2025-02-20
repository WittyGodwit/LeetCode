class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        res = ['0'] * length
        if "".join(res) in nums:
            for i in range(length, 0, -1):
                res[i - 1] = '1'
                if "".join(res) not in nums:
                    break
        return "".join(res)