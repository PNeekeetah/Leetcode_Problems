# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:45:17 2021

@author: Nikita
"""

class Solution:
    def countSquares(self, matrix: list) -> int:
        def findSquare(grid : list, square_size : int, position : tuple) -> bool:           #my solution with a glorious O(n^5) complexity
            pos_x, pos_y = position
            all_ones = True
            if (pos_x + square_size > len(grid)) or (pos_y + square_size > len(grid[0])):
                return False
            else:
                for a in range(pos_x, pos_x + square_size):
                    for b in range(pos_y, pos_y + square_size):
                        all_ones = all_ones and grid[a][b]
                        if not all_ones:
                            return False

            return True

        total_squares = 0
        for i in range (len(matrix)):
            for j in range(len(matrix[0])):
                for k in range(1, min(len(matrix),len(matrix[0])) + 1 ):
                    total_squares += findSquare(matrix,k,(i,j))
        
        return total_squares
    

    def countSquares1(self,matrix :list) -> int:         # Not my solution, got logic from friend
        count = 0
        total = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and j > 0 and matrix[i][j]:
                    matrix[i][j] = 1 + min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                count = matrix[i][j] + count
                
        print(matrix)
        return count
                   
    
"""
34 mintues : thrown in the towel
My friend's solution does the following :
    
    - starting from the second element along the main diagonal,
it sums the element at that position on the grid with the minimum
of the 3-tuple formed by the Upper, Left and Upper-Left elements.
If all 3 are 1, then the number on the grid becomes 2. A count of
2 indicates that a 2 by 2 square is present. When all 3 adjacent values
are 2, it means that the next element forms a 3 by 3 square and so on.

My algorithm is as stupid as it gets. N^2 from the start, then another
N traversals, and then for each traversal we do another (1...N)^2. Very likely,
N^5 -> only 1 teraoperations. 
    
"""