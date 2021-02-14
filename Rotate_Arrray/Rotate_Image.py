# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:57:17 2020

@author: Nikita
"""
import cv2 
import copy
import AccurateTime
import numpy as np
import matplotlib.pyplot as plt

class Solution():
    
    def __init__(self):
        None
        
    def rotate (self, matrix: list) -> list:
        newMat = copy.deepcopy(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = newMat[cols-1-col][row]
    
    # Won't work on images since they use NDARRAY
    def transpose_reverse (self, matrix: list) -> list:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range (rows):
            for j in range(i, rows):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        for row in matrix:
            row.reverse()
        
    
    def rotate90 (self, matrix: list) -> list:
        rows = len(matrix)
        cols = len(matrix[0])
        aux = 0
        for i in range(rows//2):
            for j in range(i,cols-i-1):
                aux = matrix[i][j]
                matrix[i][j] = matrix[rows-j-1][i]
                matrix[rows-j-1][i] = matrix[rows-i-1][cols-j-1]
                matrix[rows-i-1][cols-j-1] = matrix[j][cols-i-1]
                matrix[j][cols-i-1] = aux
                
    def rotate180 (self, matrix: list) -> list:
        rows = len(matrix)
        cols = len(matrix[0])
        aux = 0
        for i in range(rows//2):
            for j in range(i,cols-i-1):
                aux = matrix[i][j]
                matrix[i][j] =   matrix[rows-i-1][cols-j-1]
                matrix[rows-i-1][cols-j-1] = aux
                
                aux = matrix[rows-j-1][i]
                matrix[rows-j-1][i] = matrix[j][cols-i-1]
                matrix[j][cols-i-1] = aux
                
    def rotate270 (self, matrix: list) -> list:
        rows = len(matrix)
        cols = len(matrix[0])
        aux = 0
        for i in range(rows//2):
            for j in range(i,cols-i-1):
                aux = matrix[i][j]
                matrix[i][j] = matrix[j][cols-i-1]
                matrix[j][cols-i-1] = matrix[rows-i-1][cols-j-1]
                matrix[rows-i-1][cols-j-1] = matrix[rows-j-1][i]
                matrix[rows-j-1][i] = aux
                
"""
    i, j                          -> left to right, top to bottom
    j,len(l)-i-1                  -> up to bottom, right to left
    len(l)- j - 1, len(l) - i - 1 -> right to left, down to up
    i, len(l) - j - 1             -> down to up, left to right

"""

"""
    The idea is to rotate a matrix clockwise WITHOUT builidng a new matrix
    
    Usng the deepcopy library and being allowed to build a new matrix is really
    easy:
        
        newMat = copy.deepcopy(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = newMat[cols-1-col][row]
                
    Takeaway :
        This can't be done in O(n) time and O(1) space apparently.
        The solution, as described on SO and LC is to consider the 
        outer shells as they go towards the inside of the matrix.
        
        After this message, i have written a function that reads 
        the same matrix in 8 different ways (up->down, left->right... right->left,
        down-> up). Check for reference.
        
        Consider the following :
            ***-
            \*--
            \\=-
            \===
            
        * elements go left to right first, top to bottom second
        - elements go top to bottom first, right to left second
        = elements go right to left first, bottom top second
        \ elements go bottom top first, left to right second
            
            
            
"""
     
def main(test_case = 0):
    if (test_case == 0):
        print("Assert that black and white images are rotated 90 degrees")
        image1 = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
        
        image2 = [[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20],
                  [21,22,23,24,25]]
        
        image3 = [[1,2],
                  [3,4]]
        
        image190cw = [[7,4,1],
                      [8,5,2],
                      [9,6,3]]
        
        image290cw = [[21, 16, 11, 6, 1], 
                      [22, 17, 12, 7, 2], 
                      [23, 18, 13, 8, 3], 
                      [24, 19, 14, 9, 4], 
                      [25, 20, 15, 10, 5]]
        
        image390cw = [[3,1],
                      [4,2]]
        
        solution = Solution()
        
        
        solution.bestSolution(image1)
        solution.bestSolution(image2)
        solution.bestSolution(image3)

        assert(image1 == image190cw )
        assert(image2 == image290cw )
        assert(image3 == image390cw )
        
    elif(test_case == 1):
        print("Flip an image using 2 different algorithm 10 times to calculate average duration")
        # Read and square image
        image = cv2.imread('Rotate_Image.jpg')
        image = image[:,:,0]
        rows = len(image)
        cols = len(image[0])
        image = image[:cols,:cols] if (cols < rows) else image[:rows,:rows]
                
        # Rotation and total time
        trials = 10
        solution = Solution()
        delta = 0
        for i in range (trials):
            begin = AccurateTime.micros()
            solution.rotate(image)
            delta += (AccurateTime.micros() - begin)
            #print("Finished " + str(i) + " memory allocation iterations")
        
        print ("It took " + str(delta/1000000) + 
               " seconds to rotate via allocating more memory")
        print("It takes " + str(delta/1000000/trials) + 
               " seconds on average to rotate via memory allocation.")
        
        delta = 0
        for i in range (trials):
            begin = AccurateTime.micros()
            solution.rotate90(image)
            delta += (AccurateTime.micros() - begin)
            #print("Finished " + str(i) + " in place iterations")
            
        print ("It took " + str(delta/1000000) + 
               " seconds to rotate via O(n^2) method")
        print("It takes " + str(delta/1000000/trials) + 
               " seconds on average to rotate via O(n^2) method.")
        
        
        
    elif (test_case == 2):
        print("Perform trials on increasingly larger images to find time difference between 2 image rotation algorithms")
        # Read and square image
        image = cv2.imread('Rotate_Image.jpg')
        image = image[:,:,0]
        rows = len(image)
        cols = len(image[0])
        image = image[:cols,:cols] if (cols < rows) else image[:rows,:rows]
        reduction_factor = 16
        
        # Time vectors
        solution = Solution()
        memalloc = []
        nsquared = []
        
        timenow = AccurateTime.millis()
        
        delta = 0
        for i in range (2,len(image)//reduction_factor):
            copy = image[:i,:i] 
            begin = AccurateTime.micros()
            solution.rotate(copy)
            delta += (AccurateTime.micros() - begin)
            memalloc.append(delta/1000000)
            delta = 0
            
        delta = 0
        for i in range (2,len(image)//reduction_factor):
            copy = image[:i,:i]
            begin = AccurateTime.micros()
            solution.rotate90(copy)
            delta += (AccurateTime.micros() - begin)
            nsquared.append(delta/1000000)
            delta = 0
        
        print("It took " + str((AccurateTime.millis() - timenow)/1000 ) + 
              " seconds to complete " + str(len(image)//reduction_factor-2) +
              " operations")
        
        mem_y = np.array(memalloc)
        nsq_y = np.array(nsquared)
        x_axis = np.linspace(2,len(mem_y)+2,num = len(memalloc))
        
        plt.figure()
        plt.plot(x_axis,mem_y, color = "#FF0000",label = "O(n) memory and O(n) time" )
        plt.plot(x_axis,nsq_y, color = "#0000FF",label = "O(n^2) time and O(1) memory")
        plt.legend()
        plt.title("Rotation time as a function of image size")
        plt.xlabel("Image size in pixels")
        plt.ylabel("Time in seconds")
        
        plt.figure()
        diff = nsq_y - mem_y
        plt.plot(x_axis,diff, color = "#FF00FF",label = "Nsq - Memalloc time difference" )
        plt.title("Difference in time between the functions")
        plt.xlabel("Image size in pixels")
        plt.ylabel("Difference in time between the 2 algorithms")
        plt.legend()
        
    elif(test_case == 3):
        print(" Rotate an image using 4 different rotation algorithms")
        # Read and square image
        image = cv2.imread('Rotate_Image.jpg')
        image = image[:,:,0]
        rows = len(image)
        cols = len(image[0])
        image = image[:cols,:cols] if (cols < rows) else image[:rows,:rows]
        scale = 0.125
        
        # Show normal
        solution = Solution()
        copy = cv2.resize(image,(0,0),fx = scale, fy = scale)
        cv2.imshow("Normal",copy)
        cv2.waitKey(0) 
        
        # Show 90 degrees
        img90 = np.copy(image)
        solution.rotate90(img90)
        copy = cv2.resize(img90,(0,0),fx = scale, fy = scale)
        cv2.imshow("90 Degrees rotated",copy)
        cv2.waitKey(0)
        
        #Show 180 degrees
        img180 = np.copy(image)
        solution.rotate180(img180)
        copy = cv2.resize(img180,(0,0),fx = scale, fy = scale)
        cv2.imshow("180 Degrees rotated",copy)
        cv2.waitKey(0)
        
        #Show 270 degrees
        img270 = np.copy(image)
        solution.rotate270(img270)
        copy = cv2.resize(img270,(0,0),fx = scale, fy = scale)
        cv2.imshow("270 Degrees rotated",copy)
        cv2.waitKey(0)
        
        cv2.destroyAllWindows() 
    
    elif(test_case == 4):
        print("Show the 8 different ways of iterating through a matrix")
        sel1 = True
        
        x = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    
        y = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]
            
        l = x if sel1 else y
        
        # This is how the matrix is supposed to be gone through 
        for i in range(len(l)//2):
            print("\n")
            for j in range(i,len(l)-i-1):
                print(str(l[i][j]), end = " ")
                print(str(l[len(l)-j-1][i]), end = " ")
                print(str(l[len(l)-i-1][len(l)-j-1]), end = " ")
                print(str(l[j][len(l)-i-1]), end = " ")
        
        print("\n Horizontal first")
        
        for i in range (len(l)):                # 1.left to right, 2.up to down FIRST CHOICE *
            print("\n")
            for j in range (len(l)):
                print(str(l[i][j]), end = " ")
        print()
        
        for i in range (len(l)):                # 1.left to right, 2.down to up
            print("\n")
            for j in range (len(l)):
                print(str(l[len(l)-i-1][j]), end = " ")
        print()
        for i in range (len(l)):                # 1. right to left, 2.down to up * THIRD CHOICE =
            print("\n")
            for j in range (len(l)):
                print(str(l[len(l) - i - 1][len(l)-j-1]), end = " ")
        print()
        for i in range (len(l)):                # 1. right to left, 2.up to down
            print("\n")
            for j in range (len(l)):
                print(str(l[i][len(l)-j-1]), end = " ")
        
        print("\n Vertical now first")
        
        for j in range (len(l)):                # 1.up to down, 2.left to right, 
            print("\n")
            for i in range (len(l)):
                print(str(l[i][j]), end = " ")
        print()
        
        for j in range (len(l)):                # 1.down to up, 2.left to right, FOURTH CHOICE=
            print("\n")
            for i in range (len(l)):
                print(str(l[len(l)-i-1][j]), end = " ")
        print()
        for j in range (len(l)):                # 1.down to up , 2. right to left, 
            print("\n")
            for i in range (len(l)):
                print(str(l[len(l) - i - 1][len(l)-j-1]), end = " ")
        print()
        for j in range (len(l)):                # 1. up to down, 2. right to left,  SECOND CHOICE -
            print("\n")
            for i in range (len(l)):
                print(str(l[i][len(l)-j-1]), end = " ")

if __name__ == "__main__":
    test_case = 2
    main(test_case)
    
