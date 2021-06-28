# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 21:13:44 2021

@author: Nikita
"""

"""
This solution beats 59.21% of the submissions in terms of runtime and
it beats 41% in terms of memory.

Sure, not the shortest or the most elegant deign, but the inspiration
becomes immediately apparent when looking at the #SORTING EXAMPLE

I'm actually happy with how this turned out.
"""


class ModularPipe:
    def __init__(
        self,
        module :  "ModularPipe" = None,
    ):
        self.value = -1
        self.module = module
        self.index = -1
    
    def __str__(self):
        return self.value
    
    def update (
        self,
        value : int, 
        index : int
    ) -> None:
        if value > self.value:
            # If the value is larger, pass along the currently stored values
            if self.module is not None:
                self.module.update(self.value, self.index)
            self.value = value
            self.index = index
        else:
            # Else, pass the values since they might be larger than the ones in the module
            if self.module is not None:
                self.module.update(value, index)
    
    def get_index(self):
        return self.index
    
    def get_value(self):
        return self.value

def find_largest_two_indices(array : list) -> (int,int):
    module2 = ModularPipe()
    module1 = ModularPipe(module2)
    for index,number in enumerate(array):
        module1.update(number,index)
    return (
        module1.get_index(),
        module2.get_index(),
    )

class Solution:
    def dominantIndex(self, nums: list) -> int:
        index1,index2 = find_largest_two_indices(nums)
        if index1 != -1 and index2 == -1:
            return index1
        elif index1 != -1 and index2 != -1:
            if nums[index1] >= 2*nums[index2]:
                return index1
        return -1
    
import random

# SORTING EXAMPLE
GENERATE_NUMBERS = 100
array = [random.randint(1,100) for i in range(GENERATE_NUMBERS)]
modular_pipe_end = ModularPipe()
modular_pipe_list = [modular_pipe_end]
for i in range(1,GENERATE_NUMBERS):
    last_pipe = modular_pipe_list[-1]
    new_pipe = ModularPipe(last_pipe)
    modular_pipe_list.append(new_pipe)
    
first_pipe = modular_pipe_list[-1]
for index, number in enumerate(array):
    first_pipe.update(number,index)

sorted_array = []
for pipe in modular_pipe_list:
    sorted_array.append(pipe.get_value())
    
array.sort()

assert(array == sorted_array)
    
