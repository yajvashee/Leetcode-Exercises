class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        import math
        output = []
        for i in range(rowIndex + 1):
            ans = math.factorial(rowIndex)/(math.factorial(i) * math.factorial(rowIndex - i))
            output.append(int(ans))
        return output