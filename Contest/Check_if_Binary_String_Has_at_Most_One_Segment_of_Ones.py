# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:49:14 2021

@author: Nikita
"""

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        number = int(s,2)
        
        if (number % 2 == 0):
            while ( number % 2 == 0):
                number //= 2
            while ( number % 2 == 1):
                number //= 2
            if (number != 0):
                return False
            
        elif(number % 2 == 1):            
            while (number%2 == 1):
                number //= 2
            if (number != 0):
                return False
            
        return True
    
    
"""
I submitted this for a weekly contest. Sadly, not enough
memory and runtime distributions are available to tell me how well
i've done. 

Anyhow, it took me about 15 to 20 minutes to solve it. The runtime 
is 24 milliseconds. Submission accepted the first time.


"""