class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = ['a', 'b', 'c']
        string = []
        def generate(c: chr, happy: string, length: int):
            happy += c
            length -= 1
            if length == 0:
                string.append(happy)
                return
            for char in s:
                if char != happy[-1]:
                    generate(char, happy, length)
        for char in s:
            generate(char, "", n)
        string.sort()
        return string[k - 1] if len(string) > k - 1 else ""