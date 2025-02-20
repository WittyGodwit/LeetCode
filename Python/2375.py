class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = []
        store = 0
        for i in range(n):
            if pattern[i] == 'I':
                res.append(i + 1)
                if store:
                    res += [i - j for j in range(store)]
                    store = 0
            else:
                store += 1
        res.append(n + 1)
        if store:
            res += [n - j for j in range(store)]
        return "".join(map(str, res))