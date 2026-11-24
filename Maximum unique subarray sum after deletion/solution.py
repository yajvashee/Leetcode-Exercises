class Solution:
    def maxSum(self, nums: List[int]) -> int:
        new_nums = []
        total = 0
        if max(nums) <= 0:
            return max(nums)
        for num in nums:
            if num not in new_nums and num > 0:
                new_nums.append(num)
                total+=num
        return total