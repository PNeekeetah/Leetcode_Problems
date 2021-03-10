# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:00:24 2021

@author: Nikita
"""
        # 1-9 single digits - 9 single digits 9*10^0 + 2*9*10^1 + 3*9*10^2 + 4*9*10^3
        # 

class Solution:
    def findNthDigit(self, n: int) -> int: 
        limits = [1,9]
        digits = 1
        while (n > limits[1]):
            limits[0] = limits[1] + 1
            digits += 1
            limits[1] += digits*9*10**(digits-1)
        advance = (n - limits[0])//digits
        pos = (n - limits[0])%digits
        starting_number = 1*10**(digits-1)
        return str(starting_number + advance)[pos]       
    
    def findNthDigit1(self, n: int) -> int: #Friend's solution
        n2=n
        a=1
        b=9
        mul=1
        while (n2-(b-a+1)*mul>0):
            n2=n2-(b-a+1)*mul
            a=a*10
            b=b*10+9
            mul=mul+1
        t=(n2-1)//mul
        n2=n2-mul*t
        a=a+t
        ans=0
        while (mul-n2>0):
            a=a//10
            mul=mul-1
        ans=a%10
        return ans


solution = Solution()
h = solution.findNthDigit1(2899)
for i in range(1,30000):
    assert(str(solution.findNthDigit1(i)) == solution.findNthDigit(i))

"""
Succesful submission in 1 hour , 51 minutes and 43 seconds. Solution
beats 95.59% in terms of runtime and 91.47 in terms of memory.

Now, I had the logic behind this problem pinned down within the first 15 minutes. 
I tried submitting it at 29 minutes and 56, but I messed up 2 test cases out of 70.
Great, a flaw in my logic! The issue was the following :
    I was searching for n in the range (10**digits, 9*10^0 + 2*9*10^1 + 3*9*10^2 + 4*9*10^3...)
    I should have sought for n in the range (9*10^0 + 2*9*10^1 + 3*9*10^2 + 4*9*10^3... + 1, 9*10^0 + 2*9*10^1 + 3*9*10^2 + 4*9*10^3 ...)

Yes, I did waste 1 hour and 20 trying to figure where on earth I've mistaken the 
logic. Kudos to my friend who found the solution in about 45 minutes. 

I have 1 digit between 1 and 9. Starting range is 1, ending range is 9. 
I have 2 digits between 10 and 99. Starting range is 10, ending range is 189
""" 