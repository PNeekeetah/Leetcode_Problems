class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = list()
        self.aux_stack = list()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        
    def pour_stacks(self, remove_first : bool = False):
        while self.stack :
            self.aux_stack.append(self.stack.pop())
        
        if remove_first:
            element = self.aux_stack.pop()
        else: 
            element = self.aux_stack[-1]
        
        while self.aux_stack:
            self.stack.append(self.aux_stack.pop())
        
        return element
    
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.pour_stacks(True)
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.pour_stacks(False)
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()