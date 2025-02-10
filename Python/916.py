class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        most = {}
        for word in words2:
            count = {}
            for char in word:
                most[char] = max(most.get(char, 0), count.get(char, 0) + 1)
        res = []
        for word in words1:
            count = {}
            for char in word:
                count[char] = count.get(char, 0) + 1
            if all(count.get(char, 0) >= most[char] for char in most):
                res.append(word)
        return res