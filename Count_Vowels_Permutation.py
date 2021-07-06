# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:11:09 2021

@author: Nikita
"""

"""
Beats 14% in terms of runtime and 22% in
terms of memory consumption.

First time submission succesful.

Oh. I just realised this was a hard problem.

**************************************************
*FIRST HARD PROBLEM I EVER SOLVED ON LEETCODE <3 *
**************************************************

"""

def a(target : int, seen_dict):
    target -= 1
    
    if target == 0:
        return 1

    if seen_dict.get(("e",target)) is not None:
        value_e = seen_dict[("e",target)]
    else:
        value_e = e(target, seen_dict)
        seen_dict[("e",target)] = value_e    
    
    return value_e

def e(target : int, seen_dict):
    target -= 1
    
    if target == 0:
        return 1
    
    if seen_dict.get(("a",target)) is not None:
        value_a = seen_dict[("a",target)]
    else:
        value_a = a(target, seen_dict)
        seen_dict[("a",target)] = value_a
    
    if seen_dict.get(("i",target)) is not None:
        value_i = seen_dict[("i",target)]
    else:
        value_i = i(target, seen_dict)
        seen_dict[("i",target)] = value_i
    
    return value_a + value_i

def u(target : int, seen_dict):
    target -= 1
    
    if target == 0:
        return 1
    
    if seen_dict.get(("a",target)) is not None:
        value_a = seen_dict[("a",target)]
    else:
        value_a = a(target, seen_dict)
        seen_dict[("a",target)] = value_a
 
    return value_a

def i(target : int, seen_dict):
    target -= 1
    
    if target == 0:
        return 1
    
    if seen_dict.get(("a",target)) is not None:
        value_a = seen_dict[("a",target)]
    else:
        value_a = a(target, seen_dict)
        seen_dict[("a",target)] = value_a
    
    if seen_dict.get(("u",target)) is not None:
        value_u = seen_dict[("u",target)]
    else:
        value_u = u(target, seen_dict)
        seen_dict[("u",target)] = value_u
    
    if seen_dict.get(("e",target)) is not None:
        value_e = seen_dict[("e",target)]
    else:
        value_e = e(target, seen_dict)
        seen_dict[("e",target)] = value_e    
    
    if seen_dict.get(("o",target)) is not None:
        value_o = seen_dict[("o",target)]
    else:
        value_o = o(target, seen_dict)
        seen_dict[("o",target)] = value_o
        
    return value_a + value_e + value_o + value_u

def o(target : int, seen_dict):
    target -= 1

    if target == 0:
        return 1
     
    if seen_dict.get(("i",target)) is not None:
        value_i = seen_dict[("i",target)]
    else:
        value_i = i(target, seen_dict)
        seen_dict[("i",target)] = value_i
    
    if seen_dict.get(("u",target)) is not None:
        value_u = seen_dict[("u",target)]
    else:
        value_u = u(target, seen_dict)
        seen_dict[("u",target)] = value_u
            
    return value_i + value_u

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        seen_dict = dict()
        accumulator = 0
        
        for function in [a,i,u,e,o]:
            accumulator += function(n,seen_dict)
        
        return accumulator % (10**9 + 7)

        