# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:03:07 2020

@author: Nikita
"""

"""
1. Iterate through the first list
2. Create a new entry in a dictionary where you append 1
   whenever you encounter the element
3. Repeat steps 1-2 for list 2, but append 2 rather than 1
4. Select smaller list
5. Create a set from that list
6. Append a number equal to the minimum 
   between the 1's and 2's of the dictionary to a common terms list
"""

list1 = [1,2,3,4,5,6,7,1,2,3,4,1,2,1,2,1]
list2 = [1,2,3,4,1,1,2,3,1,1,2,1]

def my_solution(list1,list2):
    diction = {}
    for elem in list1:
        if (diction.get(elem) is None):
            diction[elem] = [1]
        else:
            diction[elem].append(1)
            
    for elem in list2:
        if (diction.get(elem) is None):
            diction[elem] = [2]
        else:
            diction[elem].append(2)
    
    common_terms = []
    small_list = list1 if len(list1) < len(list2) else list2    
    if (len(list1) > len(list2)):
        small_set = set(small_list)
        for elem in small_set:
            if (diction.get(elem) is not None):
                entry = diction[elem]
                ones = entry.count(1)
                twos = entry.count(2)
                common_terms = common_terms + [elem]*min(ones,twos)            
    
    return common_terms



# Coding the fastest time solution
def fastest_solution(list1,list2):
    diction = {}
    small_list,big_list = (list1,list2) if len(list1) < len(list2) else (list2,list1)    
    
    for elem in big_list:
        if (diction.get(elem) is None):
            diction[elem] = 1
        else:
            diction[elem] += 1
    
    common_terms = []
    
    for elem in small_list:
        if (diction.get(elem) is not None) and diction.get(elem) > 0 :
            diction[elem] -= 1
            common_terms.append(elem)
    
    return common_terms
    
common_terms_mine = my_solution(list1,list2)
common_terms_fastest = fastest_solution(list1,list2)

"""
    Takeaway:
        My solution created a hash map and counted occurences via 
        ticks. I then created a set of the smaller set, and appended
        the same number of elements as the minimum number of ticks 
        between 1 and 2.
        
        The fastest solution used a hash map and simply used accumulators
        to count the occurences. The elements of the bigger list are 
        first added to the hash map.
        Then, when iterating through the second list, we decrease the 
        accumulator in the hash map by 1 and the element is appeneded.
        This eliminates the need to convert to a set.
        
    Follow up questions which i should answer :    
    
    What if the given array is already sorted? How would you optimize your algorithm?
    
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?



"""
