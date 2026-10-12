class Solution:
    def hammingWeight(self, n: int) -> int:
        start = 1
        count = 1
        count_bits = 0
        while n > start * 2:
            start *=2
            count +=1
        start *=2
        while start >=1:
            if n >= start:
                count_bits +=1
                n -= start
            start /=2
        return count_bits