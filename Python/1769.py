class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        count = 0
        operations = 0
        for i in range(n):
            res[i] += operations
            count += int(boxes[i])
            operations += count
        count = 0
        operations = 0
        for i in range(n - 1, -1, -1):
            res[i] += operations
            count += int(boxes[i])
            operations += count
        return res