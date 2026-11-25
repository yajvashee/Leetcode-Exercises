class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = 0
        for i in range(1,n+1):
            if i % m == 0:
                print(i , '-')
                total -= i
            else:
                print(i , '+')
                total +=i
        return total 