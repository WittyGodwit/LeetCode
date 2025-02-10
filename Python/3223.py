class Solution:
    def minimumLength(self, s: str) -> int:
        memo = {}
        for char in s:
            if char in memo:
                memo[char] += 1
            else:
                memo[char] = 1
        length = 0
        for num in memo.values():
            if num <= 2:
                length += num
            elif num % 2 == 0:
                length += 2
            else:
                length += 1
        return length