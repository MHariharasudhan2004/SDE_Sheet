class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        st.append(nums2[0])
        res=[]
        mapping={}
        for i in range(1,len(nums2)):
            while st and st[-1]<nums2[i]:
                mapping[st[-1]]=nums2[i]
                st.pop()
            st.append(nums2[i])
        for i in st:
            mapping[i]=-1
        for i in range(len(nums1)):
            res.append(mapping[nums1[i]])
        return res
                
        