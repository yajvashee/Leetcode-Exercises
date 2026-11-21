class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        occurences = {}
        for num in nums:
            if num in occurences:
                occurences[num] +=1
            else:
                occurences[num] = 1
        for key,value in occurences.items():
            if value == 1:
                continue
            elif value == 2:
                return True
            else:
                count = 0
                for i in range(2,value):
                    if value % i == 0:
                        count +=1
                if count == 0:
                    return True
        return False