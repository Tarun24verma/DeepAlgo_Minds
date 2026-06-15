from collections import deque

class MyStack:
    def __init__(self):
        self.inqueue = deque()
        self.outqueue = deque()
        self._top = None
    
    def push(self, x: int) -> None:
        self.inqueue.append(x)
        self._top = x
    
    def pop(self) -> int:
        while len(self.inqueue) > 1:
            self._top = self.inqueue[0]
            self.outqueue.append(self.inqueue.popleft())
        value = self.inqueue.popleft()
        self.inqueue, self.outqueue = self.outqueue, self.inqueue
        return value
    
    def top(self) -> int:
        return self._top
    
    def empty(self) -> bool:
        return not self.inqueue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()