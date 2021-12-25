class MyQueue:

    def __init__(self):
        self.values1 = []
        self.values2 = []

    def push(self, x: int) -> None:
        self.values1.append(x)
            
    def pop(self) -> int:
        if self.values2:
            return self.values2.pop()
        
        elif self.values1:
            val = 0
            for i in range(len(self.values1)-1):
                val = self.values1.pop()
                self.values2.append(val)
            return self.values1.pop()
        else: 
            return None
                
                
    def peek(self) -> int:
        if self.values2:
            return self.values2[-1]
        elif self.values1:
            val = 0
            for i in range(len(self.values1)):
                val = self.values1.pop()
                self.values2.append(val)
            return self.values2[-1]
        else:
            return None
        
        

    def empty(self) -> bool:
        if self.values1 or self.values2:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()