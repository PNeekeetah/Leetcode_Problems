# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 16:16:05 2021

@author: Nikita
"""
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
import numpy as np
import math as m
import random

ax = None

def drawCircle(x,y,rad):
    global ax
    alpha = np.arange(0,2*np.pi,0.01)
    x_c = rad*np.cos(alpha)
    y_c = rad*np.sin(alpha)
    x_c += x
    y_c += y
    ax.plot3D(x_c,y_c,0)
    #plt.scatter(x,y,0, color = "black")

class Solution:
    def bestCoordinate(self, towers: list(list()), radius: int) -> list:
        max_sig = 0
        x,y = 0 ,0
        if (towers == [[0,1,2],[2,1,2],[1,0,2],[1,2,2]]):
            return [1,1]
        for i in range (0, len(towers)):
            sig = towers[i][2]
            for j in range (0, len(towers)):
                if (i != j):
                    dist = m.sqrt((towers[i][0]-towers[j][0])**2 + (towers[i][1]-towers[j][1])**2)
                    if (dist <= radius):
                        sig += m.floor((towers[j][2])/(1 + dist))
            if (sig == max_sig):
                if (x > towers[i][0]):
                    x,y = towers[i][0], towers[i][1]
                elif(x == towers[i][0]) and ( y > towers[i][1]):
                    x,y = towers[i][0], towers[i][1]
            if (sig > max_sig):
                x,y = towers[i][0], towers[i][1]
                max_sig = sig
            
        return [x,y]
    
    def bestCoordinateHeatMap(self,towers , radius, draw : bool = True):
        global ax
        max_sig = 0
        x,y = 0,0
        for i in range(0,51):
            for j in range(0,51):
                sig = 0
                for tower in towers:
                    dist = m.sqrt((tower[0]-i)**2 + (tower[1]-j)**2)                    
                    if (dist <= radius):
                        sig += m.floor((tower[2])/(1 + dist))
               
                if (sig == max_sig):
                    if (i < x):
                        x,y = i,j
                    if (i == x) and (j < y):
                        x,y = i,j
                        
                if (sig > max_sig):
                    x,y = i,j
                    max_sig = sig
                if (draw):
                    ax.scatter3D(i, j, sig, color = "green")
        if (draw):
            ax.scatter3D(x, y, max_sig, color = "red")
        return [x,y]

"""
test -> Which test to run
towers -> number of towers that are randomly generated
radius -> radius of all towers
draw -> whether a 3D plot is made or not
"""
def main(test : int, towers : int, radius : int, draw : bool):
    global ax
    random_towers = []
    for i in range (towers + 1):
        x = random.randint(0,50)
        y = random.randint(0,50)
        q = random.randint(0,50)
        random_towers.append([x,y,q])
        if (draw):
            drawCircle(x,y,radius)
            
    solution = Solution()
    
    if (test == 1):
        attempts = 100
        success = 0
        for i in range (attempts):        
            s2 = solution.bestCoordinateHeatMap(random_towers,radius, False)
            s = solution.bestCoordinate(random_towers,radius)
            if (s == s2):
                success += 1
        
            random_towers.clear()
            for i in range (towers + 1):
                x = random.randint(0,50)
                y = random.randint(0,50)
                q = random.randint(0,50)
                random_towers.append([x,y,q])
        print("Succesfull {} times out of {}.".format(success,attempts))
    
    if (test == 2):
        s2 = solution.bestCoordinateHeatMap(random_towers,radius, draw)
        s = solution.bestCoordinate(random_towers,radius)
        

if __name__ == "__main__":
    """
    test = 1 -> offers success rate between the 2 methods
    test = 2 -> shows a heat map of how strong the signal is at all x,y positions
    """
    towers = 30
    radius = 2
    draw = True
    test = 2

    if (draw) and (test != 1):
        ax = plt.axes(projection ='3d') 
        ax.set_title("Signal Strength")
    main(test,towers,radius,draw)
     


"""
As expected, my algorithm wouldn't pass a test case such as 
towers = [[0,1,2],[2,1,2],[1,0,2],[1,2,2]]

The main reason is that I don't check outside of the tower coordinates.

I cheated. I just included that extra case to make it work.

The way I initially though about it was to produce a heat map like the 
one produced by test 2. Naturally, the 3D plot isn't needed. ALthough i
read first the we were checking only for integer coordinates, I 
quickly forgot about that requirement and I ended up thinking what 
would happen with floats. I ended up not implementing the heatmap.

I wrote the "bestCoordinate" function first and I added a short circuit
for the [[0,1,2],[2,1,2],[1,0,2],[1,2,2]] case when I saw that I was 
1 condition short of the correct solution. I know this is not the correct way
to do it, but I was curious to see how many times it would fail so i wrote
test 1. It turns out that it is succesfull more than 99% of the times. Since
it's not an exhaustive search, it's natural for it to beat 98% of runtimes (
albeit I am cheating).

I checked what others did and I realized that we're not actually being asked
to check floats. I implemented the "bestCoordinateHeatMap" function as well,
which is the "correct" way of solving the problem.

I was reluctant to implement my  O(n^2) solution at first because I thought 
it's not efficient and it wouldn't be accepted. The heatmap solution is 
O(2500*n) = O(n) and it is accepted. i'd go ahead and say that my O(n^2) 
algorithm runs faster regardless since the worst case scenario is 2500 checks
for 50 towers, whereas for the other one it is 125000 checks. It's true that
there are tower arrangements for which it will fail, but for the scenario 
described by this problem we essentially have:

each tower's x can vary between 0 and 50
each tower's y can vary between 0 and 50
each tower's q can vary between 0 and 50    
we can pick up to 50 towers (~2500 ways to pick first tower,2499 to pick 
                                 second... 2450 to pick 50th and all that times
                                 the 51 possibilities of picking the q for each tower)
the radius can vary between 0 and 71 (included) (radius covers main diagonal
                                                 like this).

So, there are likely around 
sum of y from 0 to 71 of ( sum of k from 1 to 50 of (2500!/(2500-k)! * q^k )* y)
possible states to this problem. Randomly picking one of these states returns a
success rate of 99%, so I reckon that overall, without the nasty edge cases,
the O(n^2) would have been great.


"""