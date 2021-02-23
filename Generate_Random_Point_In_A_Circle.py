# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:40:21 2021

@author: Nikita
# Credit to my friend EIS for the solution randPoint2
# Credit to my other friend RCM for the solution randPoint2

"""

import matplotlib.pyplot as plt
import random 
import numpy as np

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
    
    def randPoint(self) -> list:
        y = random.uniform(self.y_center - self.radius,  self.y_center + self.radius )
        term = ((self.radius - y + self.y_center)*(self.radius + y - self.y_center))**(1/2)
        x = random.uniform(self.x_center - term ,self.x_center + term )
        return [x,y]
    
    def randPoint1(self) -> list:
        x= 2**31
        y= 2**31
        while ((x-self.x_center)**2+(y-self.y_center)**2 > self.radius**2):
            x = self.x_center - self.radius + self.radius*2*random.uniform(0,1) 
            y = self.y_center - self.radius + self.radius*2*random.uniform(0,1)
        return [x,y]
    
    def randPoint2(self) -> list:
        alpha = random.uniform(0, 2*np.pi)
        s_rad = self.radius*math.sqrt(random.uniform(0,1))
        x = s_rad*np.cos(alpha) + self.x_center
        y = s_rad*np.sin(alpha) + self.y_center
        return [x,y]         

# Initialize Solution with these points
y_c = -73839.1
x_c = -3289891.3
r = 0.01
solution = Solution(r,x_c,y_c)

# Draw circle
y_1 = np.arange(y_c - r, y_c + r, r/10000)
x_1 = [x_c + np.sqrt((r - i + y_c)*(r + i - y_c)) for i in y_1]
x_2 = [x_c - np.sqrt((r - i + y_c)*(r + i - y_c)) for i in y_1]
scatter = [solution.randPoint() for i in range (100000)]    
points = np.array(scatter).transpose()

# Plot
plt.plot(x_1,y_1)
plt.plot(x_2,y_1)
plt.scatter(points[0],points[1],color = "red")
plt.axes()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Circle randPoint scatter")
plt.show()

"""
My initial approach was rather mathematical (and inefficient). Vectors are
easier than analysis, I should have learned this to this day.

Nonetheless, implementation 2 is inspired by my friends' idea
that had to do with sampling. Fully aware it's inefficient, but I wanted
to do it that way too.

I also appreciate the third idea that my other friend suggested, using 
a rotation vector and a tranlation vector to move it to the center
of the circle. 

It's worth noting that none of these submissions actually worked.
Mine and my friend's are too slow. For some reason, 
the accepted submissions included a math.sqrt(random.random()) function.
I do not understand why, and it remains a mystery for me.

This submission can be considered a failure as far as I'm concerned.
"""