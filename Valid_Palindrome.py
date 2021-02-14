# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:16:34 2020

@author: Nikita
"""
import re
class Solution:
    
    def __init__(self) -> None:
        pass
    
    def isPalindromeRe(self, s: str) -> bool:
        s = re.sub("[^A-Za-z0-9]", "", s).lower()
        p = s[:(len(s)+1)//2-1:-1]
        return (s[:(len(s))//2] == p)
        
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
    
        while (start < end):
            is_a_char1 = s[start].isalnum()
            is_a_char2 = s[end].isalnum()
            
            if (is_a_char1 and is_a_char2): 
                if not(s[start].lower() == s[end].lower()):
                    return False
           
            start += is_a_char2 or not is_a_char1
            end -= is_a_char1 or not is_a_char2
         
        return True

def main():
    testcase1 = "A man, a plan, a canal: Panama"
    testcase2 = "\" `b93\"a\"?\"aQ39b` Q"
    
    solution = Solution()
    assert(solution.isPalindromeRe(testcase1) == True)
    assert(solution.isPalindromeRe(testcase2) == False)
        
if __name__ == "__main__":
    main()
            


"""
Improvements roadmap:
1. First method had:
    - a dictionary of all characters
    - a for loop to get rid of all non alphanumeric chars
    - extra storage allocated for a new, reversed string
    - a return statement where it we checked if all chars were equal
    Runtime - around 340 ms, beats 6% of submissions

2. In the second iteration, i got rid of the extra storage allocated to 
reverse the string via palindrome = string[::-1]. It had
    - a dictionary of all alphanumeric chars
    - a while loop with 2 indices, one at the start and one at the end
    - a palindrome variable that was set to false whenever a pair of 
    mismatched characters was encountered
    Runtime - around 100 ms, beats 35% of all submissions

3. Having the dictionary in memory slows down the function call. Getting rid 
of it improves the runtime by 100%. Now, each charcter is checked via 
isalpha() and via isdigit(). Now the function has
    - a while loop with 2 indices, one at the start and one at the end
    - a palindrome variable that was set to false whenever a pair of 
    mismatched characters was encountered
    Runtime - Around 50 miliseconds, beats 71 % of all submissions
    
4. There is a join method called isalnum() that checks if the char is 
alphanumeric. same as 3. Same runtime as 3

5. Rather than having an if-elif-else list to drop through, i decided to 
increment the steps at the end regardless: the formulas are
  start += is_a_char2 or not is_a_char1
  end -= is_a_char1 or not is_a_char2
  Runtime - Not too much of an improvement
  
I can't think of any other improvements i could bring here. 

The best solution used re/ before taking a look at it. I know how fast re is,
but I didn't want to import a library. 

1. First iteration with re beats 98.96 % of submissions in terms of time. 
It does:
    1. strip string of all non alpha numeric
    2. take a s
    
2. Second iteration beats 99.84% of all submissions/ I learned better how 
slices work and rather than doing
        p = s[:(len(s)+1)//2][::-1] i am doing p = s[:(len(s)+1)//2-1:-1]
 Code remained unchanged.

My solution is quite good as it is, so even if the best solution beats it by
a couple of miliseconds, i like mine better for its elegance.

"""
