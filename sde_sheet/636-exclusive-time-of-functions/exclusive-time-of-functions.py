class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res=[0]*n
        call_stack=[]
        start_t=0
        for log in logs:
            id,sig,stamp=log.split(":")
            id=int(id)
            stamp=int(stamp)
            if sig=="start":
                if call_stack:
                    res[call_stack[-1]]+=stamp-start_t
                call_stack.append(id)
                start_t=stamp
            else:
                res[call_stack.pop()]+=stamp-start_t+1
                start_t=stamp+1
        return res



            
        