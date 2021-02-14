# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:47:57 2020

@author: Nikita
"""


class Solution:
    
    def __init__(self) -> None:
        pass
    
    # Best soltution on LeetCode
    def best_solution(self, x : int) -> int:
        s = x < 0
        x =((-1)**s) * int((str(abs(x))[::-1]))
        return x if x.bit_length() < 32 else 0
    
    # My solution
    def reverse(self, x : int) -> int:
        x = str(x)
        start = int((x[0] == "-"))
        end = len(x) - 1
        new_int = ""
        for i in range (end, start - 1, -1):
            new_int +=  x[i]
            
        new_int = (-1)**start * int (new_int)
        return 0 if ((new_int < -2**31) or (new_int > 2**31 - 1)) else new_int
        
def main():
    test_case_list = [1,-412,2929,1000000000000000000, 32154,-5123]
    test_results = [1,-214, 9292, 1, 45123, -3215]
    solution = Solution()
    solution_results = []
    
    for elem in test_case_list:
        solution_results.append(solution.reverse(elem))
        
    for i in range (len(test_results)):
        try:
            assert(test_results[i] == solution_results[i])
        except AssertionError:
            print("Failed at index " + str(i) + " for values "
                  + str((test_results[i], solution_results[i])))
    
    
if __name__ == "__main__":
    main()
    
    
"""
    Takeaway:
        The fastest method did 3 steps: 
            1) it checked the sign
            2) it abs(x) is converted to string an reversed via [::-1]
            3) it returns the (-1)**sign if the integer had less than 32 bits
    
    My method allocated a new array and did one pass through all elements.
"""