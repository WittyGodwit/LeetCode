class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        count = [0] * (n + 1)
        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            count[start] += shift
            count[end + 1] -= shift
        total = [0] * n
        cumulation = 0
        for i in range(n):
            cumulation += count[i]
            total[i] = cumulation
        res = []
        for i, char in enumerate(s):
            char = chr((ord(char) - ord('a') + total[i]) % 26 + ord('a'))
            res.append(char)
        return "".join(res)