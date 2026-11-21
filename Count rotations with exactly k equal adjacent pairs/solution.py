class Solution:
    def countRotations(self, s: str, k: int) -> int:
        count = 0
        for i in range(len(s)):
            word = s[i-len(s):] + s[0:i]
            score = 0
            for j,letter in enumerate(word):
                if j == len(word) - 1:
                    continue
                else:
                    if letter == word[j+1]:
                        score +=1
            if score == k:
                count +=1
        return count