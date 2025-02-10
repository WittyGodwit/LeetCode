class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        nums3 = {}
        for i in nums1:
            nums3[i] = nums3.get(i, 0) + len2
        for j in nums2:
            nums3[j] = nums3.get(j, 0) + len1
        res = 0
        for key, value in nums3.items():
            if value % 2:
                res ^= key
        return res