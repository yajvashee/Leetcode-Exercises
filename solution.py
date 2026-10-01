class Solution:
    def addBinary(self, a: str, b: str) -> str:
        number_a = 0
        number_b = 0
        for i in range(len(a)-1,-1,-1):
            number_a += (2 **i) * int(a[len(a) - 1 - i])
        for i in range(len(b) -1,-1,-1):
            number_b += (2**i) * int(b[len(b) - 1 - i])
        total = number_a+number_b
        return bin(total)[2:]