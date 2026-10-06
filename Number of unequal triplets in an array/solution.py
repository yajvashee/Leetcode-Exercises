class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i <j and j<k:
                        if nums[i] !=nums[j] and nums[i] != nums[k] and nums[k] != nums[j]:
                            count+=1
        return count