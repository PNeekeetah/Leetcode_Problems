from typing import List 

"""
Beats 78% in terms of runtime
Beats 0% in terms of memory 

Second submission was succesful 
because I messed up the dequeue
function the first time.
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = -1
        self.capacity = k
        self.elements = 0
        self.array : List[int] = [None for _ in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.tail = (self.tail + 1) % self.capacity
        self.array[self.tail] = value
        self.elements += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.array[self.head] = None
        self.head = (self.head + 1) % self.capacity

        self.elements -= 1
        
        if self.isEmpty():
            self.head = 0
            self.tail = -1
            
        return True 

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.array[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.array[self.tail]
        

    def isEmpty(self) -> bool:
        return self.elements == 0
        

    def isFull(self) -> bool:
        return self.elements == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()