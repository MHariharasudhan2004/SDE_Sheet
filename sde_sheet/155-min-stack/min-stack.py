class MinStack:
    from collections import deque
    def __init__(self):
        self.st=deque()
        

    def push(self, val: int) -> None:
        self.st.append(val)
        

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        m=min(self.st)
        return m
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()