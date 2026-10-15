class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        occurence = {}
        count = 0
        for char in s:
            if char not in occurence:
                occurence[char] = 1
            else:
                occurence[char] +=1
        occurence = {k: v for k, v in sorted(occurence.items(), key=lambda item: item[1],reverse = True)}
        if len(occurence) > k:
            for i in range(k,len(occurence)):
                count += list(occurence.values())[i]
        return count