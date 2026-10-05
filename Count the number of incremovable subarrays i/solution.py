class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sub_array = nums[0:i] + nums[j+1:len(nums)]
                res = all(x < y for x, y in pairwise(sub_array))
                if res == True:
                    count+=1
        return count

                