# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:32:36 2020

@author: Nikita
"""

import numpy as np

# Test cases
board1 = [ ["5","3",".",".","7",".",".",".","."]
          ,["6",".",".","1","9","5",".",".","."]
          ,[".","9","8",".",".",".",".","6","."]
          ,["8",".",".",".","6",".",".",".","3"]
          ,["4",".",".","8",".","3",".",".","1"]
          ,["7",".",".",".","2",".",".",".","6"]
          ,[".","6",".",".",".",".","2","8","."]
          ,[".",".",".","4","1","9",".",".","5"]
          ,[".",".",".",".","8",".",".","7","9"]]

board2 =  [  ["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

def checkDuplicates(array: np.array) -> bool:
    dictionary = {}
    for elem in array:
        if ((dictionary.get(elem) is None)):
           dictionary[elem] = 1
        elif(elem != "."):
            return False
    return True

class Solution():
    
    def __init__(self):
        None
        
    def bestSolution(self, board1: [[str]]) -> bool:
        
        # First, find the height and width of the board
        # A sudoku square always has side 3
        r = len(board1)
        c = len(board1[0])
        l = 3
        
        # Create 9 sets of rows, 9 sets of columns, 9 sets of squares
        # rows and cols is a unidimensional list of sets, squs is a bidimensional
        # list of lists of sets
        rows = [set() for _ in range(r)]
        cols = [set() for _ in range(c)]
        squs = [[set() for _ in range(r//l)] for _ in range (c//l)]
        
        for row in range(r):
            for col in range(c):
                # only do an operation if the character is not "."
                if (board1[row][col] != "."):
                    char = board1[row][col]
                    
                    # Try to add character in a row set. If it's not possible
                    # it was found previously in the same row.
                    if char not in rows[row]:
                        rows[row].add(char)
                    else: 
                        return False
                    
                    # Try to add character in a col set. If it's not possible,
                    # it was found previously in the same column.
                    if char not in cols[col]:
                        cols[col].add(char)
                    else:
                        return False
                    
                    # Try to add character in a square set. If it's not possible,
                    # it was found previously in the same square.
                    if char not in squs[row//l][col//l]:
                        squs[row//l][col//l].add(char)
                    else:
                        return False
        return True
        
    def isValidSudoku (self, board: [[str]]) -> bool:
        numpyboard = np.array(board)
        valid = True

        # Iterates through rows
        for i in range (len(numpyboard)):
            valid = valid and checkDuplicates(numpyboard[i,:]) 
            if (not valid):
                return False
        
        # Iterates through columns
        for i in range (len(numpyboard)):
            valid = valid and checkDuplicates(numpyboard[:,i]) 
            if (not valid):
                return False
        
        # Iterates through squares
        for i in range (len(numpyboard)//3):
            for j in range(len(numpyboard)//3):
                valid = valid and checkDuplicates(np.asarray(
                    numpyboard[i*3:(i+1)*3,j*3:(j+1)*3]).reshape(-1))
                if (not valid):
                    return False
        
        return True

solution = Solution()
verity = solution.bestSolution(board2)



"""

We have to check as follows :
    First, check all rows. board[i][j] , i first, j second
    [0][:], [1][:], [2][:], [3][:], [4][:], [5][:], [6][:], [7][:], [8][:], [9][:]         
    
    Second, check all columns. board[i][j], i second, j first
    [:][0], [:][1], [:][2], [:][3], [:][4], [:][5], [:][6], [:][7], [:][8], [:][9]

    Third, we must check 9 squares.
    [0:3][0:3], [0:3][3:6], [0:3][6:9]
    [3:6][0:3], [3:6][3:6], [3:6][6:9]
    [6:9][0:3], [6:9][3:6], [6:9][6:9]
    
I know the method is painfully slow and that I shouldn't use numpy arrays,
but i didn't want to deal with list indexing.

My solution was pretty deep into the bad tail end of the distribution.

    Takeaway:
        Essentially, my solution iterates through the whole board 3 times.
        It thus comes as no surprise that my solution is 3 times as slow
        as the fastest solution
        
        The fastest solution iterates through the whole board ONLY once.
        For example, element at 0,0 belongs to row 0, column 0 and square 0,0
        Element at 3,8 belongs to row 3, column 8 and to square 1,2
        If The element was previously found in said row, column or square, the
        algorithm can just quit. No np.arrays needed.

"""