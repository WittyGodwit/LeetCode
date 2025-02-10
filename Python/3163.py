class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        index = 0
        length = len(word)
        while index < length:
            char = word[index]
            count = 1
            while index + 1 < length and word[index + 1] == word[index]:
                count += 1
                index += 1
            while count > 9:
                comp += f"9{char}"
                count -= 9
            comp += f"{count}{char}"
            index += 1
        return comp