# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:53:49 2021

@author: Nikita
"""
"""
total_arr = []
import matplotlib.pyplot as plt

for n in range (0,10000):
    total = 0
    for i in range (0, n):
        if (str(bin(i)).find("11") == -1):
            total += 1
    total_arr.append(total)

plt.plot (total_arr)
plt.show()

"""

import AccurateTime as AT
import matplotlib.pyplot as plt

def sol (number, add_1 : bool ,seen = None):
    global n
    
    if (seen == None):
        seen = {}
    
    if (number > n):
        return
    
    if not (seen.get(number)):
        seen[number] = len(seen)    
        sol(number*2,False,seen )
        if not (add_1):
            sol(number*2 + 1,True,seen )
        
    return seen


def sol_iter(number, add_1 : bool):
    global n    
    stack = []
    total = 0
    stack.append( (number,add_1) )
    while (len(stack) > 0):
        current_item = stack.pop()
        if not(current_item[0] > n):
            total += 1
            if not(seen.get(current_item[0])):
                seen[current_item[0]] = 1
                if not(current_item[1]):
                    stack.append((current_item[0] << 2 + 1,True))    
                stack.append((current_item[0] << 2,False))
        
    return len(seen) 

sol_r = []
sol_i = []
test_start = AT.millis()

n = 10**9 
#sol_r.append()
dict = sol(0,0)    

#for i in range (10**9):
#    n = i 
    
    #start = AT.millis()
#    sol_r.append(sol(0,0))
    #end = AT.millis() - start
    #sol_r.append(end/1000.0)
    
#    start = AT.millis()
#    print(sol_iter(0,0))
#    end = AT.millis() - start
#    sol_i.append(end/1000.0)
    
#test_end = (AT.millis() - test_start)//1000.0
#print("Test ended after {}".format(test_end))    
#print("It took {} seconds on average for recursive calls".format(sum(sol_r)/len(sol_r)))
#print("It took {} seconds on average for iterative calls".format(sum(sol_i)/len(sol_i)))

#plt.plot(sol_r)
#plt.plot(sol_i)
#plt.show()

"""
Solution runs well, but not well enough. Iterative method probably runs better.
It finds solution for 10**9 in like 2 seconds or less, whereas the O(n^2) 
method can't. It even finds a solution for 10**10.




"""