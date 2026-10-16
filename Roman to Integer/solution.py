class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0

        for index, char in enumerate(s):
            if index == len(s) - 1:
                total += symbol_value[char]
            elif symbol_value[char] < symbol_value[s[index + 1]]:
                total -= symbol_value[char]
            else:
                total += symbol_value[char]

        return total