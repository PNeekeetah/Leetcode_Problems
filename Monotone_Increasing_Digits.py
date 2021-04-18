# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:16:13 2021

@author: Nikita

The whole idea is to :
    1. Split number into digits
    2. Find the longest monotonically increasing sublist; can coincide with
    list of digits, in which case return the list of digits instead
    3. Find an index in the sublist where we can safely subtract 1 and 
    still maintain the monotonic increasing property
    4. Subtract 1 from that point and set the rest equal to 9.
"""

class Solution:
    # Second solution, split into logic blocks
    def monotoneIncreasingDigits(self, N: int) -> int:
        # Separates the number into its member digits
        def getDigits(number: int) -> list:
            digits = []
            while number > 0:
                digits.append(number%10)
                number //= 10
            digits.reverse()
            return digits
        # For every 2 digits d_i, d_(i+1), check that d_i < d_(i+1) and that 
        # i+1 is a valid index within the list of digits
        def lowerAndBounded(digits: list, index : int) -> bool:
            return ((index < len(digits)-1) and 
                    (digits[index] <= digits[index+1]))
        # Find the point where d_i > d_(i+1)
        def findTurningPoint(digits: list) -> int:
            turning_index = 0
            while lowerAndBounded(digits,turning_index):
                turning_index += 1
            return turning_index
        # Find an index i such that d_(i+1) remains larger than d_(i)
        # even after subtracting 1
        def findSubtractionIndex(digits: list, index: int) -> int:
            while (digits[index]-1 < digits[index-1]) and index >= 1:
                index -= 1
            return index
        # From an index I, set all digits to 9
        def setNines(digits: list, index: int) -> list:
            for i in range(index, len(digits)):
                digits[i] = 9
            return digits
        # For an input list, get the corresponding number
        def reassembleNumber(digits: list) -> int:
            number = 0
            for digit in digits:
                number = number*10 + digit
            return number
        """Logic start
        """
        digits = getDigits(N)
        turning_point = findTurningPoint(digits)
        if turning_point + 1 == len(digits):
            return N
        turning_point = findSubtractionIndex(digits,turning_point)
        digits = setNines(digits,turning_point+1)
        digits[turning_point] -= 1
        return reassembleNumber(digits)
    
    # First solution
    def monotoneIncreasingDigits1(self, N: int) -> int: 
        aux = N
        digits = []
        while aux > 0:
            digits.append(aux%10)
            aux //= 10
        digits.reverse()
        index = 0
        place = 0
        for i in range(len(digits)-1):
            if digits[i] <= digits[i+1]:
                continue
            else:
                place = i
                break
        else:
            return N
        print(place)
        while digits[place]-1 <  digits[place-1] and place >= 1:
            place -= 1
        for i in range(place+1, len(digits)):
            digits[i] = 9
        digits[place] -= 1
        print(digits)
        number = 0
        for digit in digits:
            number = number*10 + digit
        return number      

solution = Solution()
hello = solution.monotoneIncreasingDigits(1232)

"""
for i in range (100000):
    a = monotoneIncreasingDigits(i)
    dic[i] = (a,i-a)
"""

"""
2 cases : either it's a number that has itself a monotonically increasing
structure, or it is 1 that doesn't have that.

In the second case, we have to find 
"""

"""

19241
18999

20001
19999

41241
39999

12343
12339

12339

99997


9 9 9 9 7
8 9 9 9 9

7 8 9 2 3

6 7 3 9 2 8
6 6 9 9 9 9

2 8 2 4 1 9 9 1  
2 7 9 9 9 9 9 9   

"""