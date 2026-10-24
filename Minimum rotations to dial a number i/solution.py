class Solution:
    def minRotations(self, s: str) -> int:
        total = 0
        position = 0
        digits = [i for i in range(10)]
        for i,char in enumerate(s):
            if int(char) - position > 5:
                total += (10 +position - int(char))
            elif int(char) - position < -5:
                total += (int(char) - position + 10)
            else:
                total += (abs(int(char) -position))
            position = int(char)
        return total