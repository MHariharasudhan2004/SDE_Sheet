class MinStack:
    from collections import deque
    def __init__(self):
        self.st=deque()
        self.minst=deque()
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minst or self.minst[-1]>=val:
            self.minst.append(val)

        

    def pop(self) -> None:
        if self.st:
            val=self.st.pop()
            if self.minst and val==self.minst[-1]:
                self.minst.pop()
            
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        if self.minst:
            return self.minst[-1]
        return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()