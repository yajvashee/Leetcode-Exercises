class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater_list = []
        for i,nums in enumerate(nums1):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j,len(nums2)):
                        if nums2[k] > nums2[j]:
                            next_greater_list.append(nums2[k])
                            break
                        elif k == len(nums2) - 1:
                            next_greater_list.append(-1)
        return next_greater_list            