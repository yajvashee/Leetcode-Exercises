class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        product = 1
        for i in range(2):
            product *= max(nums) - 1
            nums.remove(max(nums))
        return product