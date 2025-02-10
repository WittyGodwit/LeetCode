class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        memo = []
        for i in range(len(s)):
            if s[i] in memo:
                continue
            memo.append(s[i])
            index = len(s) - 1
            while(s[i] != s[index]):
                index -= 1
            res += len(set(s[i + 1:index]))
        return res