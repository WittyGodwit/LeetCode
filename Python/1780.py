class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = int(math.log(n, 3))
        while power >= 0:
            if n >= 3 ** power:
                n -= 3 ** power
                if n >= 3 ** power:
                    return False
            else:
                power -= 1
        return not n