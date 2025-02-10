class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        start = 0
        for i in range(len(arr)):
            if sorted(arr[start:i]) == list(range(start, i)):
                start = i
                result += 1
        return result