# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 18:26:34 2021

@author: Nikita
"""

"""
Beats 21% in terms of runtime and 9% in terms of memory.

Took 40 minutes write this.

Special thanks to my friend E who suggested looking for
numbers with a unique character.
"""

def reduce_numbers(char, chars_dict, number_dict):
    multiplier = 0
    if chars_dict.get(char) is not None and chars_dict.get(char) > 0:
        multiplier = chars_dict.get(char)
        for num_char in number_dict.keys():
            chars_dict[num_char] -= multiplier*number_dict[num_char]
    return multiplier

def build_numbers_dict(chars_dict):
    numbers_dict = { i : 0 for i in range(10)}
    four_dict = {"f" : 1, "o" : 1, "u" : 1, "r" : 1}
    six_dict = {"s" : 1, "i" : 1, "x" : 1 }
    eight_dict = {"e" : 1, "i" : 1, "g" : 1 , "h" : 1, "t" : 1 }
    two_dict = {"t" : 1, "w" : 1, "o" : 1}
    zero_dict = {"z" : 1, "e" : 1, "r" : 1, "o" : 1}
    seven_dict = {"s" : 1, "e" : 2, "v" : 1 , "n" : 1} # got rid of all S's by now
    five_dict = {"f" : 1, "i" : 1, "v" : 1, "e" : 1} # got rid of all V's by now
    three_dict = {"t" : 1, "h" : 1, "r": 1, "e" :2 } # got rid of all T's by now
    one_dict = {"o" : 1, "n" : 1, "e" : 1} # got rid of all O's by now
    nine_dict = {"n" : 2, "i" : 1, "e" : 1} # only nines remain
    numbers_dict[4] = reduce_numbers("u",chars_dict, four_dict)
    numbers_dict[6] = reduce_numbers("x",chars_dict, six_dict)
    numbers_dict[8] = reduce_numbers("g",chars_dict, eight_dict)
    numbers_dict[2] = reduce_numbers("w",chars_dict, two_dict)
    numbers_dict[0] = reduce_numbers("z",chars_dict, zero_dict)
    numbers_dict[7] = reduce_numbers("s",chars_dict, seven_dict)
    numbers_dict[5] = reduce_numbers("v",chars_dict, five_dict)
    numbers_dict[3] = reduce_numbers("t",chars_dict, three_dict)
    numbers_dict[1] = reduce_numbers("o",chars_dict, one_dict)
    numbers_dict[9] = reduce_numbers("i",chars_dict, nine_dict)
    return numbers_dict

class Solution:
    def originalDigits(self, s: str) -> str:
        chars_dict = dict()
        for char in s:
            chars_dict.setdefault(char,0)
            chars_dict[char] += 1
        print(chars_dict)
        numbers_dict = build_numbers_dict(chars_dict)       
        
        string = ""
        for i in range(0,10):
            if numbers_dict.get(i) is not None and numbers_dict.get(i) > 0:
                for j in range(numbers_dict.get(i)):
                    string += str(i)
        return string