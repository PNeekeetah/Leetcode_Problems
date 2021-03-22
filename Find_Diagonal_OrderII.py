# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:38:52 2021

@author: Nikita
"""

class Solution:
    def findDiagonalOrder(self, nums: list()) -> list():  #My attempt that failed
        lower_x = 0
        upper_x = len(nums)
        lower_y = 0
        upper_y = 0
        solution = []
        for i in range(upper_x):
            upper_y = max(upper_y,len(nums[i]))
        
        X = 0
        Y = 0

        while X <= upper_x - 1:
            tX = X
            tY = 0
            while tY <= min(X,upper_y-1) and tX >= 0: 
                if len(nums[tX]) > tY:
                    solution.append(nums[tX][tY])
                tY += 1
                tX -= 1
            X += 1
        Y += 1
        while Y <= upper_y - 1:
            tX = X-1
            tY = Y
            while tX >= 0 and tY <= upper_y - 1:
                if len(nums[tX]) > tY:
                    solution.append(nums[tX][tY])
                tX -= 1
                tY += 1
            Y += 1
                    
        return solution
    
    def findDiagonalOrder1(self,nums:list()) -> list(): # Not my concept
        c = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if (c.get(i+j) != None):
                    c[i+j].insert(0,nums[i][j])
                else:
                    c[i+j] = [nums[i][j]]
                    
        solution = []
        for diags in c.values():
            solution.extend(diags)
        
        return solution
        




"""
I failed this submission and I gave up after about 2 hours.

First attempt : Get maximum size_x (length of input array) and then get size_y
(input of longest array from input array). Then, in this M*N matrix, iterate
across the secondary diagonals of this "imaginary" square matrix. 
If the element with the given 2 indices exists in the main array, append it to
the solution. See "findDiagonalOrder".

I knew this worked, and I also assumed that you can't do any better, especially
after seeing their second hint (append to a tuple sum of indices and indices, 
sort by indices).

My solution was , worst case, N*M / in their case, it was x * M*N *log(x*M*N)
where x is between 0.0 and 1.0. x*M*N represents how many elements there are 
in the matrix. If x represents the solution to the above 
equation, then X goes from 50% for a 10 elements maximum matrix to 5% for a 10^8 
maximum elements matrix. (for a 10^8 matrix, you have to have under 5*10^6 
elements for the sorting approach to be efficient)

The quadratic solution worked just fine for 53 out of 57 cases. Since they 
suggested the sorting solution, I assumed that was the best possible runtime
for this problem. The last 4 cases seemed WAAAY too exceptional (less than 1%
fill when such a matrix has on average 50% fill?).

Well, it is true that their hint is on average worse than quadratic. However,
there is a better option which is linear in the number of elements / see 
"findDiagonalOrder1" above. That is linear in the number of elements, no more, 
no less. 




There are 2*N - 1 secondary diags
a00                 - I = 0; J = 0 -> I increases
a10, a01            - I = 1; J = 0 -> J decreases
a20, a11, a02       - I = 2; J = 0
a30, a21, a12, a03
a31, a22, a13
a32, a23
a33 

Initially, I increases from 0 to N -> J Increases as I decreases
Then,      I stays the same for another N-1 and J starts increasing; J increases as I decreases

"""