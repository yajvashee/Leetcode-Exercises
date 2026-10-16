class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        even_numbers = [num for num in nums if num % 2 == 0]
        print(even_numbers)
        num1 = 0
        for num in even_numbers:
            num2 = num
            num1 = num1 | num2
        return num1