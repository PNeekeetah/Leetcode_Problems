# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:06:40 2021

@author: Nikita
"""

import numpy as np

class Solution:
    
    def generateMatrix(self, n: int) -> list: # Friend's work
        mat=[[0 for i in range(n)] for i in range(n)]
        x=[0,0]
        y=(0,1)
        for i in range(1,n**2+1):
            mat[x[0]][x[1]]=i
            if (mat[(x[0]+y[0])%n][(x[1]+y[1])%n] > 0):
                y=(y[1],-1*y[0])
            x[0]=x[0]+y[0]
            x[1]=x[1]+y[1]
        return mat
    
    def generateMatrix(self, n: int) -> list:  # My own submission
        mat = np.zeros([n,n], dtype=int)
        start_x = 0
        start_y = 0
        end_x = n - 1
        end_y = n - 1
        modus = 0
        x,y = 0,0
        num = 1
        while (start_x <= end_x) and ( start_y <= end_y ):
            if (modus == 0):
                # x increases    
                x , y = start_x, start_y
                
                while ( x <= end_x):
                    mat[y][x] = num
                    num += 1
                    x += 1
                
                start_y += 1
                modus += 1
                modus %= 4
            elif (modus == 1):
                # y increases
                x , y = end_x, start_y
                
                while ( y <= end_y):
                    mat[y][x] = num
                    num += 1
                    y += 1
                

                end_x -= 1
                modus += 1
                modus %= 4
            elif (modus == 2):
                # x decreases
                x , y = end_x, end_y
                
                while ( x >= start_x):
                    mat[y][x] = num
                    num += 1
                    x -= 1
                

                end_y -= 1
                modus += 1
                modus %= 4
            elif (modus == 3):
                # y decreases
                x , y = start_x , end_y
                
                while ( y >= start_y):
                    mat[y][x] = num
                    num += 1
                    y -= 1
                

                start_x += 1
                modus += 1
                modus %= 4

        return mat

        
solution = Solution()
matrix = np.array(solution.generateMatrix(20))
print(matrix)
"""
This is my submission for the Spiral II matrix. I also added my friend's
work as well for future reference.

It can certainly be done a lot faster, but I will first have a look 
at something else.

"""