class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        n=len(nums1)
        b=(n+1)//2
        print(b)
        if n%2==1:
            return nums1[b-1]
        else:
            l=0
            h=n-1
            mid=(l+h)//2
            res=(nums1[mid]+nums1[mid+1])/2
            return res

        