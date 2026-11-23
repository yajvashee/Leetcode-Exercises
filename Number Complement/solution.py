class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        total = 0
        for i in range(len(bin_num)-1,-1,-1):
            if bin_num[len(bin_num) - 1 - i] == "0":
                print(len(bin_num) - 1 - i)
                total += 2 **(i)
        return total