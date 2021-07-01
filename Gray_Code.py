# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 23:50:06 2021

@author: Nikita
"""

"""
I had grand ideas for this problem. I thought I identified  the 
correct pattern (i.e. what you see in the comments in XorUnit).
When I coded that, it turns out that it wasn't correct. 

Then I looked up Karnaugh Maps since I recall that they
were build such that each element differs by 1 bit.I was
planning on doing a smart traversal and then returning 
that. 

Whilst showering, I thought I might implement something akin to 
what is inside Solution.

First time submission was a success. It beats 45% in terms of
runtime annd 11.40 percent in terms of memory usage. This 
was part of "Daily Challenges" and somehow I submitted my 
solution before 12 AM (11:59 PM!). I've been mulling over
this problem for the past 12 hours hoping i'd implement 
something smart and elegant. Well, not really 12 hours since
i've been working at least 7 hours and cooked and did other 
things for another 2, but still.
"""

class Solution:
    def grayCode(self, n: int) -> List[int]:
        strt = ["0","1"]
        for i in range(1,n):
            next_0 = [("0"+elem) for elem in strt]
            next_1 = [("1"+elem) for elem in strt]
            next_1.reverse()
            next_0.extend(next_1)
            strt = next_0

        final = [int(elem,2) for elem in strt]
        return final
    
"""
DIR_RIGHT = "right"
DIR_LEFT = "left"
DIR_DICT = {
    DIR_RIGHT : DIR_LEFT,
    DIR_LEFT : DIR_RIGHT,
}

class XorUnit:
    def __init__ (self, bits : int):
        self.xor_factor = "{value:0>{bits}s}".format(
            value=str(1),
            bits=bits,
        )
        self.max_rotations = 2**bits
        self.exec_rotations = 0
        self.next_direction = DIR_LEFT
        self.bits = bits
        self.rotations_to_execute = 1
        self.remaining_rotations_cycle = 1

    def _rotate_left(self):
        #print("LEFT")
        self.xor_factor = self.xor_factor[1:] + self.xor_factor[0]  
        return self
    
    def _rotate_right(self):
        #print("RIGHT")
        self.xor_factor = self.xor_factor[-1] + self.xor_factor[0:-1]
        return self
    
    def _rotate(self, direction : str):
        if direction == DIR_LEFT:
            self._rotate_left()
        else:
            self._rotate_right()
    
    def _execute_rotation(self):
        if self.remaining_rotations_cycle > 0:
            self.remaining_rotations_cycle -= 1
        elif self.remaining_rotations_cycle == 0 and self.next_direction == DIR_RIGHT:
            self.remaining_rotations_cycle = self.rotations_to_execute - 1
            self.next_direction = DIR_DICT[self.next_direction]
        else:
            self.rotations_to_execute *= 2
            self.remaining_rotations_cycle = self.rotations_to_execute - 1
            self.next_direction = DIR_DICT[self.next_direction]
            
        self._rotate(self.next_direction)
        self.exec_rotations += 1


    def _get_xor_factor(self):
        return self.xor_factor
    
    def get_and_rotate(self):
        xor_factor = self._get_xor_factor()
        #print(xor_factor)
        self._execute_rotation()
        return int(xor_factor,2)
    
        
number = 0 
grey_seq = [number]
xor_unit = XorUnit(4)

LONG_SEQ = ["00","01","11", "10"]
SHORT_SEQ = ["0","1"]

class KarnaughModule:
    def __init__(self, long_seq : bool = False, next_module : "KarnaughModule" = None):
        self.index = 0
        self.sequence = SHORT_SEQ
        self.length = 2
        if long_seq:
            self.sequence = LONG_SEQ
            self.length = 4
        self.next_module = next_module
        
    def update(self):
        self.index = (self.index + 1) % self.length
        if self.index == 0 and self.next_module is not None:
            self.next_module.update()
            
    def get_sequence(self):
        return self.sequence[self.index]
        
    def get_string(self):
        if self.next_module is not None:
            return self.next_module.get_string() + self.get_sequence()
        else:
            return self.get_sequence()
"""