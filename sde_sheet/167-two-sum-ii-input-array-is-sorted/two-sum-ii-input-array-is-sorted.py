class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        res=[]
        while l<r:
            if numbers[l]+numbers[r]<target:
                l+=1
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                res.append(l+1)
                res.append(r+1)
                l+=1
                while l<r and numbers[l]==numbers[l-1]:
                    l+=1
        return res

        