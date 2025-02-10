class Solution:
    def minChanges(self, s: str) -> int:
        index = 0
        count = [1]
        length = len(s)
        while index < length - 1:
            if s[index + 1] == s[index]:
                count[-1] += 1
            else:
                count.append(1)
            index += 1
        index = 0
        num = 0
        length = len(count)
        while index < length - 1:
            if count[index] % 2 != 0:
                num += 1
                count[index + 1] -= 1
            index += 1
        return num