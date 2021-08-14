"""
Beats 99% in terms of runtime and 73% in terms of memory.
First submission failed because I deleted something accidentally
from my code/ 

Took me about 15 minutes to come up with this.
"""
class MyQueue:
        def __init__(self):
            self.q = list()
            self.index = 0
            self.total = 0
            
        def reset(self):
            self.q.clear()
            self.index = 0
            self.total = 0
            
class MyStack:  
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = MyQueue()
        self.q2 = MyQueue()
        self.primary = self.q1
        self.secondary = self.q2
        self.modus = 0
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.primary.q.append(x)
        self.primary.total += 1
        
    def _access_last(self, remove : bool = False):
        # append all but last
        while self.primary.index < self.primary.total - 1:
            self.secondary.q.append(self.primary.q[self.primary.index])
            self.primary.index += 1
            self.secondary.total += 1
        
        # get last element
        element = self.primary.q.pop()
        if remove == False:
            self.secondary.q.append(element)
            self.secondary.total += 1
        
        # clear primary queue
        self.primary.reset()
        
        # switch queue pointers
        if self.modus == 0:
            self.primary = self.q2
            self.secondary = self.q1
            self.modus += 1
        else:
            self.primary = self.q1
            self.secondary = self.q2
            self.modus -= 1
            
        return element

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._access_last(remove = True)
        
    def top(self) -> int:
        """
        Get the top element.
        """
        return self._access_last()

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        e1 = self.primary.total == 0
        e2 = self.secondary.total == 0
        return e1 and e2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()