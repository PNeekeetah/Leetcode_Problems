# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:09:02 2021

@author: Nikita
"""

"""
Beats 85.84 % in terms of runtime. Beats 65.28% in terms of memory.
Finished this solution in 44:55 minutes.
"""

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        letter_dict = {}
        base_letter = ord("a")
        for row in range (0,5):
            for col in range (0,5):
                letter_dict[chr(base_letter + row*5 + col)] = (row,col)
        letter_dict["z"] = (5,0)
        print(letter_dict)
        current_position = (0,0)
        current_pointer = 0
        tape = ""
        while current_pointer < len(target):
            target_position = target[current_pointer]
            if letter_dict[target_position] == current_position:
                tape += "!"
            else:
                if current_position == (5,0):
                    tape += "U"
                    manhattan_distance = (letter_dict[target_position][0] - current_position[0] + 1, 
                                          letter_dict[target_position][1] - current_position[1])
                else:    
                    manhattan_distance = (letter_dict[target_position][0] - current_position[0], 
                                          letter_dict[target_position][1] - current_position[1])
                if manhattan_distance[1] < 0:
                    for i in range(0,abs(manhattan_distance[1])):
                        tape += "L"
                else:
                    for i in range(0,abs(manhattan_distance[1])):
                        tape += "R"

                if manhattan_distance[0] < 0:
                    for i in range(0,abs(manhattan_distance[0])):
                        tape += "U"
                else:
                    for i in range(0,abs(manhattan_distance[0])):
                        tape += "D"

                tape += "!"
            current_pointer += 1
            current_position = (letter_dict[target_position][0],
                                letter_dict[target_position][1])
        return tape