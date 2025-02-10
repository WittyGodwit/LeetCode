class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        par, unlocked = 0, 0
        for i in range(n):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == '(':
                par += 1
            elif par:
                par -= 1
            elif unlocked:
                unlocked -= 1
            else:
                return False
        while par and unlocked and par < unlocked:
            par -= 1
            unlocked -= 1
        return not par