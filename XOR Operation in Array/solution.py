class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [2* i + start for i in range(n)]
        num1 = 0
        for num in nums:
            num1 = num1 ^ num
        return num1