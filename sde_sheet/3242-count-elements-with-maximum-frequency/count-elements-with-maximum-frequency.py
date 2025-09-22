class Solution:
    from collections import Counter
    def maxFrequencyElements(self, nums: List[int]) -> int:
        l=Counter(nums)
        c=l.most_common(1)[0][1]
        print(c)
        cou=0
        for item,count in l.items():
            if count==c:
                cou+=c
        return cou

        