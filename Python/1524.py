class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        count, prefix = 0, 0
        odd, even = 0, 1
        for a in arr:
            prefix += a
            if prefix % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1
        return int(count % (1e9 + 7))