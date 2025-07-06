class FindSumPairs:
    from collections import defaultdict
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.arr1=nums1
        self.arr2=nums2.copy()
        self.ele_freq=defaultdict(int)
        for ele in nums2:
            self.ele_freq[ele]+=1


    def add(self, index: int, val: int) -> None:
        old_val=self.arr2[index]
        self.ele_freq[old_val] -= 1
        self.arr2[index] += val
        new_val = self.arr2[index]
        self.ele_freq[new_val] += 1
        

    def count(self, tot: int) -> int:
        res=0
        for ele in self.arr1:
            target=tot-ele
            res+=self.ele_freq.get(target,0)
        return res
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)