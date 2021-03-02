# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:40:23 2021

@author: Nikita
"""

class Solution:
    def intervalIntersection(self, firstList, secondList) :
        if (len(firstList) == 0):
            return []
        if (len(secondList) == 0):
            return []
        list1_index = 0
        list2_index = 0
        sol = []
        while (list1_index < len(firstList)) and (list2_index < len(secondList)):
            pair1 = firstList[list1_index]
            pair2 = secondList[list2_index]
            if (pair1[0] <= pair2[0]) and (pair1[1] >= pair2[1]):
                sol.append([pair2[0],pair2[1]])
                list2_index += 1
            elif (pair1[0] >= pair2[0]) and (pair1[1] >= pair2[1]) and (pair1[0] <= pair2[1]):
                sol.append([pair1[0],pair2[1]])
                list2_index += 1
            elif (pair1[0] <= pair2[0]) and (pair1[1] <= pair2[1])  and (pair2[0] <= pair1[1]):
                sol.append([pair2[0],pair1[1]])
                list1_index += 1
            elif ((pair1[0] >= pair2[0]) and (pair1[1] <= pair2[1])):
                sol.append([pair1[0],pair1[1]])
                list1_index += 1
            elif (pair1[0] > pair2[1]):
                list2_index += 1
            elif (pair2[0] > pair1[1]):
                list1_index += 1
                       
        return sol
    
    def intervalIntersection1(self, firstList, secondList) :
        if (len(firstList) == 0):
                return []
        if (len(secondList) == 0):
            return []
        list1_index = 0
        list2_index = 0
        sol = []
        while (list1_index < len(firstList)) and (list2_index < len(secondList)):
            pair1 = firstList[list1_index]
            pair2 = secondList[list2_index]
            low = min(pair1[0],pair2[0])
            high = max(pair1[1],pair2[1])
            if (low <= high):
                sol.append([low,high])
                if (pair1[1] <= pair2[1]):
                    list1_index += 1
                elif(pair1[1] >= pair2[1]):
                    list2_index += 1
            if (pair1[0] > pair2[1]):
                list2_index += 1
            if (pair2[0] > pair1[1]):
                list1_index += 1
                
        return sol
            
            
l1 = [[0,2],[5,10],[13,23],[24,25]]
l2 = [[1,5],[8,12],[15,24],[25,26]]
 
solution = Solution()
hey = solution.intervalIntersection1(l1,l2)
    
            
                
"""
Not my proudest solution.

My solution got accepted the third time around. It probably took me around 
1 hour and 20.

My very first idea was to build 2 superpositions of heaviside step functions
for both A and B, then multiply the results together.

I hate doing a mess of if else statements, but the very first solution
would have required way too much space. There is a more intelligent way
to go about this problem, I'm sure.

"""
        
            
        
        