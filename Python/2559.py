class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        v_words = []
        v_sum = [0] * (len(words) + 1)
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                v_words.append(1)
            else:
                v_words.append(0)
        for i in range(len(words)):
            v_sum[i + 1] = v_sum[i] + v_words[i]
        return [v_sum[query[1] + 1] - v_sum[query[0]] for query in queries]