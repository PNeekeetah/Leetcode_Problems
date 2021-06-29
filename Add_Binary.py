# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:03:35 2021

@author: Nikita
"""

"""
Runtime : beats 77%
Memory : beats 93%

First time submission successful.
"""

def convert_to_int(string_repr : str) -> int:
    number = int(string_repr,2)
    return number

def convert_to_string(integer : int) -> str:
    binary = bin(integer)
    #doing binary(int) returns 0b in front
    #this gets rid of that
    string_repr = "{}".format(binary[2:])
    return string_repr

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = convert_to_int(a)
        int_b = convert_to_int(b)
        sum_a_b = int_a + int_b
        string_repr = convert_to_string(sum_a_b)
        return string_repr