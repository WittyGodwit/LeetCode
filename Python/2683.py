class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        def isValid(first: int) -> bool:
            original = [0] * n
            original[0] = first
            for i in range(n):
                original[i] = original[i - 1] ^ derived[i - 1]
            return original[n - 1] ^ original[0] == derived[n - 1]
        return isValid(0) or isValid(1)