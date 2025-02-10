class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        string= ""
        last = ""
        llast = ""
        d = [['a', a], ['b', b], ['c', c]]
        while(d[0][1] or d[1][1] or d[2][1]):
            d = sorted(d, key=lambda x: x[1], reverse=True)
            if d[0][1] and not d[0][0] == last == llast:
                string += d[0][0]
                d[0][1] -= 1
                llast = last
                last = d[0][0]
            elif d[1][1]:
                string += d[1][0]
                d[1][1] -= 1
                llast = last
                last = d[1][0]
            else:
                break
        return string