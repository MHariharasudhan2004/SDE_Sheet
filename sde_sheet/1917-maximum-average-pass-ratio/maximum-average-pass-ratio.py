class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap=[]
        for p,t in classes:
            gain=(p+1)/(t+1)-p/t
            heapq.heappush(max_heap,(-gain,p,t))
        for _ in range(extraStudents):
            neg_gain,p,t=heapq.heappop(max_heap)
            p+=1
            t+=1
            new_gain=(p+1)/(t+1)-p/t
            new_neg_gain=-new_gain
            heapq.heappush(max_heap,(new_neg_gain,p,t))
        tr=0
        for new_gain,p,t in max_heap:
            tr+=p/t
        return tr/len(classes)





        