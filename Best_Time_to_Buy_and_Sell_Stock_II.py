# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:47:08 2020

@author: Nikita
"""

import numpy as np
import matplotlib.pyplot as plt

#Test cases
trial1 = [7,6,5,4,3,2,1,20,31,2]
trial2 = [7,2,21,3,4,1,23,4,1,2,3,2,1]
trial3 = [1,2,3,4,5,6,7]
trial4 = [7,6,5,4,3,2,1]
trial5 = [1,2,3,6,5,4,3,1,2,3,4,5,7,7,7,7,7,7,7,7,7,8,9,10,1,2,3,4,5,6,10,10,10,10,10,9,8,7,7,2,2,1,10]
trial6 = [1,2,3,4,5]
          
#Stock, first derivative and derivative sign/ Derivative is convolution by [-1,1]
stocks = np.array(trial5)
stodif = np.convolve(stocks,[1,-1],mode ="valid")
posneg = [np.sign(elem) for elem in stodif ]

#Axes
stocks_axis = [i for i in range(len(stocks))]
stodif_axis = [i for i in range(len(stodif))]
zeroes      = [0 for i in range(len(stodif))]

#Create a figure 
plt.figure()
plt.plot(stocks_axis,stocks, label = "Stock Variation", color = "#AA5500")
plt.plot(stodif_axis,stodif,color = "#FF00FF",label = "Derivative")
plt.plot(stodif_axis,posneg,color="#0000FF",label = "Derivative Sign" )
plt.plot(stodif_axis,zeroes,color = "#000000", label = "Zero line", linestyle="--")
plt.xlabel("Day")
plt.ylabel("Stock Value")
plt.title("Stock Value Over Time")
plt.legend()

# My submission
bought = False
boughtIndex = 0
acc = 0
for i in range(len(stodif)):
    if (not bought) and (stodif[i] > 0):
        boughtIndex = i
        bought = True 
    elif (bought and stodif[i] < 0):
        acc = acc + stocks[i]-stocks[boughtIndex]
        boughtIndex = 0
        bought = False
    elif (stodif[i] == 0):
        continue
    
if (bought):
    acc += stocks[-1] - stocks[boughtIndex]

# Best Submission in terms of space
profit = 0
for (index,number) in enumerate(stocks[:-1]):
    if (stocks[index + 1] - number > 0):
        profit += (stocks[index + 1] - number)

# Best submission in terms of time
profit1 = 0
for i in range (0,len(stocks)-1):
    if (stocks[i+1] - stocks[i] > 0):
        profit1 += stocks[i+1] - stocks[i] 
        
"""
    Takeaway : 
        The fastest solutions used the derivative like
        I did (don't know if they did it consciously), but they spotted something
        I didn't, namely, you need not care about whether you bought the 
        the stock or not, you only care about the final value.
        
        In this case, it's a lot easier to use a running difference of the form
        y[n] = x[n+1] - x[n] AS LONG AS y[n] >= 0. You don't care when
        y[n] = 0, since it doesn't affect you i
"""