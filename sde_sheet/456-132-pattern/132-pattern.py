class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st=[]
        two=float("-inf")
        for n in nums[::-1]:
            if n<two:
                return True
            while st and st[-1]<n:
                two=st.pop()
            st.append(n)
        return False        