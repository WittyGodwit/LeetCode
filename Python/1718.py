class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 2 * n - 1
        seq = [0] * length
        use = [0] * (n + 1)
        def backtrack(x: int) -> bool:
            while x < length and seq[x]:
                x += 1
            if x == length:
                return True
            for index in range(n, 1, -1):
                if use[index]:
                    continue
                if x + index < length and seq[x + index] == 0:
                    seq[x], seq[x + index] = index, index
                    use[index] = 1
                    if backtrack(x + 1):
                        return True
                    seq[x], seq[x + index] = 0, 0
                    use[index] = 0
            if not use[1]:
                seq[x] = 1
                use[1] = 1
                if backtrack(x + 1):
                    return True
                seq[x] = 0
                use[1] = 0
            return False
        backtrack(0)
        return seq