"""
Took me about 5 minutes to solve this
Beats 77% in terms of runtime.
Beats 83% in terms of memory.

I failed my first submission because I didn't
account for what would happen if the element
still existed in the stack someplace else 
when removing it from the min_stack

This was a Python 2 submission because I have
written a solution for it in Python 3 a couple
of weeks ago.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_stack = list()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        element = self.stack.pop()
        if element == self.min_stack[-1] and element not in self.stack:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
