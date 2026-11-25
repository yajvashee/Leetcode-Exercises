class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        occurences_word_1 = {}
        occurences_word_2 = {}
        for char in word1:
            if char not in occurences_word_1:
                occurences_word_1[char] = 1
            else:
                occurences_word_1[char] +=1
        for char in word2:
            if char not in occurences_word_2:
                occurences_word_2[char] = 1
            else:
                occurences_word_2[char] +=1
        abs_diff = {k: abs(occurences_word_1.get(k, 0) - occurences_word_2.get(k, 0)) for k in occurences_word_1.keys() | occurences_word_2.keys()}
        for key,value in abs_diff.items():
            if value > 3:
                return False
        return True