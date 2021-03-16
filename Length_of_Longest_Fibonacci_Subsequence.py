# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:02:32 2021

@author: Nikita
"""

class Solution:
    def lenLongestFibSubseq(self, arr: list()) -> int: # My solution
        longest_sequence = 0
        dictionary = {}
        for i in range (0, len(arr)):
            dictionary[arr[i]] = 1
            
        for i in range (0, len(arr)-1):
            for j in range(i+1, len(arr)):
                candidate = 2
                a = arr[i]
                b = arr[j]
                a, b = b, a+b
                while(dictionary.get(b)):
                    candidate += 1
                    a, b = b, a+b
                if candidate > longest_sequence and candidate > 2:
                    longest_sequence = candidate
        return longest_sequence
    
    def lenLongestFibSubseq1(self,arr): # My friend's solution
        fin=[]
        actual=[]
        ind=[]
        li=set(arr)
        max_ind=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j] in li:
                    fin.append(arr[j])
                    actual.append(arr[i]+arr[j])
                    ind.append(2)
                    max_ind=max(max_ind,2)
                while(arr[j] in actual):
                    k=actual.index(arr[j])
                    a=fin[k]
                    fin[k]=actual[k]
                    actual[k]=a+arr[j]
                    ind[k]+=1
                    max_ind=max(max_ind,ind[k])
            fin=[]
            actual=[]
            ind=[]
        return max_ind

    
"""
Solved this problem in 17 minutes and 57 seconds. It beats 50 percent
of solutions in terms of runtime and 52 in terms of memory. Second
submission succesful.

The problem was the following : instead of doing "b in array", i should
have used a dictionary. 

My solution is essentially the same as the one presented on Leetcode.
The only difference is:
    
    1: i am using an if statement rather than a max
    2: they are returning the answer only if it's greater than 2

"b in dictionary" -> linear
"dictionary.get(b)" -> O(1)
"""