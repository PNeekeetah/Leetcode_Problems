# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:24:27 2021

@author: Nikita
"""

string = ["H","e","l","l","o"," ","W","o","r","l","d"]
"""
def reversePrint(string : str, position : int):
    if (position == len(string)):
        return ""
    rev = reversePrint(string,position + 1)
    rev += string[position]
    return rev
"""
class Solution:
    
    def reverseString(self, s: list(str()),position : int) -> None:
        if (position == len(s)):
            return
        self.reverseString(s,position + 1)
        aux = s[position]
        s[position:len(s)-1] = s[position + 1 : len(s)] 
        s[len(s)-1] = aux
    
solution = Solution()
solution.reverseString(string,0)


"""
The problem required in place modifcation, but I first tried slicing.

I visualized it using the "Visualize Python" online program and I realized
I was creating copies of the List.

I noticed it cannot be done without keeping track with a position pointer 
so I tried doing something as follows : increment the position by 1, then,
when at the end, swap the n-1 elements with the n'th element recursively.
Then, after exiting the recursion, at each stage i would do:

aux = s[pointer]
s[pointer:len(s)-2] = s[pointer+1 : len(s)-1]
s[len(s)-1] = aux

This does exactly 2 swaps for the last 2 characters, 3 swaps for the last 3,
4 for the last 4... n for the last n characters. 

I was dumbfound for a bit since it passed 477 out of 478 test cases. 

The solution actually involved keeping track of the 2 ends of the list 
recursively, and then after returning from each recursive call, swap 
the elements from the middle outwards.
 
"""