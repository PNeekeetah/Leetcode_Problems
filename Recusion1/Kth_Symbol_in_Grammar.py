# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 00:37:17 2021

@author: Nikita
"""

class Solution:
    def kthGrammar(self,N: int, K: int) -> int:
        def basedOn(k : int):            
            if (k == 1) :
                return "0"
            
            if (k%2 == 1):
                lastK = basedOn((k+1)//2)
                if (lastK == "0"):
                    return "0"
                else:
                    return "1"
            else:
                lastK = basedOn(k//2)
                if (lastK == "0"):
                    return "1"
                else:
                    return "0"
                
        return basedOn(K)
        
solution = Solution()
symbol = solution.kthGrammar(5,3)
a = ""
for i in range (1,17):
    a += solution.kthGrammar(5, i)

      
     
            
"""
Submitted in 1 hour , 25 minutes and 12 seconds. I didn't take any hints.

My solution beats 59% in terms of runtime and 53% in terms of memory.

What really helped me throughout this problem was to figure out on which
character the current K is based on. E.g. Row 4 K 5 is based on row 3 k 3...
One of the things that really helped me out a lot was to write sentences
in my recursive calls that matched the structure below this.



I need to establish the relationships between the various Ks

On row 4, K 5 is based on
   row 3, K 3 is based on
   row 2, K 2 is based on
   row 1, K 1 is based on 0
   
On row 4, K 8 is based on 
   row 3, K 4 is based on
   row 2, K 2 is based on
   row 1, K 1 is based on 0
   
On row 4, K 7 is based on
   row 3, k 4 is based on
   row 2, k 2 is based on
   row 1, k 1 is based on
   
On row 5, K 13 is based on
   row 4, k 7 is based on
   row 3, k 4 is based on
   row 2, k 2 is based on
   

   
"""