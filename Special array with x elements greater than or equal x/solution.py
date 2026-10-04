class Solution:
    def specialArray(self, nums: list[int]) -> int:
        for i in range(1,max(nums) + 1):
            count = 0
            for num in nums:
                if num >= i:
                    count +=1
            if count == i:
                return count
        return -1