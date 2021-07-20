from random import randint

"""
First time submission succesful
Beats 39% in terms of runtime and 
0 % in terms of memory usage.

I cheated a bit because I recalled 
that I wrote a script in my Unity 
Sorting Algorithms repo that did
exactly this, but I couldn't remember
whether I imported a random library 
or not. I had a quick look at what
I did there and I submitted it.
"""


class Solution:

    def __init__(self, nums: List[int]):
        self.array = list(nums)
        self.shuffled = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.shuffled = list(self.array)
        return self.shuffled

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        array_length = len(self.shuffled)
        for i in range(array_length):
            rand_index = randint(0, array_length - 1)
            if rand_index == i:
                continue
            temp = self.shuffled[i]
            self.shuffled[i] = self.shuffled[rand_index]
            self.shuffled[rand_index] = temp
        return self.shuffled

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
