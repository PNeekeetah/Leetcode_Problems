'''
 # @ Author: Nikita
 # @ Creation Time: 2021-07-10 16:49:46
 # @ Last Modified: 2021-07-10 16:49:51
'''

"""
Submission without while beats 67% in terms
of runtime and 18 % in terms of memory.

First time submission succesful. Took
me 15 minutes to solve it, BUT I just
heard from my friend who was also trying 
to solve the problem that you do it using
a Greedy algorithm.

If he wouldn't have told me that, I would 
have probably tried a DP approach which would 
have taken me 2 more hours :)
"""

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibo_array = [1,1]

        while k > fibo_array[-1]:
            fibo_array.append(fibo_array[-1] + fibo_array[-2])
        
        count = 0
        for i in range(len(fibo_array)-1, -1, -1):
            while k - fibo_array[i] >= 0:
                count += 1
                k -= fibo_array[i]
            if k == 0:
                break 

        # No need for while
        """
        for i in range(len(fibo_array)-1, -1, -1):
            if k // fibo_array[i] >= 0:
                count +=  k // fibo_array[i]
                k = k - k//fibo_array[i]*fibo_array[i]
            if k == 0:
                break 
        """
        return count
            