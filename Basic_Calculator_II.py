# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:24:38 2021

@author: Nikita
"""

class Solution:
    def calculate(self, s: str) -> int:
        all_symbols = []
        numbers = { "{}".format(num) : 1 for num in range (0,10)}
        possible_number = ""
        for char in s:
            if char in numbers:
                possible_number += char
            else:
                if possible_number:
                    all_symbols.append(int(possible_number))
                if char != " ":
                    all_symbols.append(char)
                possible_number = ""
        all_symbols.append(int(possible_number))
        tape = all_symbols
        pointer = -1
        acc = 0
        while pointer < len(tape):
            temp_acc = tape[pointer + 2 - 1] 
            if tape[pointer + 2] in ['*','/']:
                while (pointer + 2 < len(tape)) and tape[pointer + 2] in ['*','/']:
                    if tape[pointer + 2] == '*':
                        temp_acc *= tape[pointer + 2 + 1]
                    elif tape[pointer + 2] == '/':
                        temp_acc //= tape[pointer + 2 + 1]     
                    pointer += 2
            else:
                while (pointer + 2 < len(tape)) and tape[pointer + 2] in ['+','-']:
                    if tape[pointer + 2] == '+':
                        temp_acc += tape[pointer + 2 + 1]
                    elif tape[pointer + 2] == '-':
                        temp_acc -= tape[pointer + 2 + 1]     
                    pointer += 2
            acc += temp_acc
            if pointer + 2 >= len(tape):
                break
        return acc
        
sol = Solution()
s = sol.calculate("1-1+1")