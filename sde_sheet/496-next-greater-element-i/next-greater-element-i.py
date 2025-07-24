class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    for k in range(j,len(nums2)):
                        if nums2[k]>nums2[j]:
                            res.append(nums2[k])
                            break
                        elif k==len(nums2)-1:
                            res.append(-1)
        return res
            

        