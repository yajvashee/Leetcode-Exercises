class Solution:
    def reverseDegree(self, s: str) -> int:
        lowercase_alphabet = list(string.ascii_lowercase)
        total = 0
        for i,char in enumerate(s):
            index_in_string = lowercase_alphabet.index(char) + 1
            total += (i+1) * (27 - index_in_string)
        return total