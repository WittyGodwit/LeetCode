class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count1, count2 = bin(num1).count('1'), bin(num2).count('1')
        if count1 == count2:
            return num1
        b = list(bin(num1)[2:].zfill(32))
        i = 0
        while count1 > count2:
            i -= 1
            if b[i] == '1':
                b[i] = '0'
                count1 -= 1
        while count1 < count2:
            i -= 1
            if b[i] == '0':
                b[i] = '1'
                count1 += 1
        return int("".join(b), 2)