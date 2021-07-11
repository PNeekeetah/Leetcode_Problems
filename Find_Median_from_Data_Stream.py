'''
 # @ Author: Nikita
 # @ Create Time: 2021-07-11 13:47:17
 # @ Modified time: 2021-07-11 13:51:03
'''

"""
Beats 6% in terms of runtime and 
93 % in terms of memory usage.

I bet there are better approaches 
out there than my O(n^2) approach here.

Took me 5 minutes to come up with this appraoch.
First submission succesful.
"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = list()

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array.sort()

    def findMedian(self) -> float:
        middle = (len(self.array) - 1)//2
        if len(self.array) % 2 == 0:
            median = (self.array[middle] + self.array[middle + 1])/2
        else:
            median = self.array[middle]
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
