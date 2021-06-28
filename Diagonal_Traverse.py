# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:39:00 2021

@author: Nikita
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:39:00 2021

@author: Nikita
"""

"""
This took me about 1 hour to code and debug :)
Beats 26.06% in terms of runtime and 7.28 %
in terms of memory.

Was it necessary to overcomplicate it like this?
Nope.
Did I enjoy doing it nonetheless?
Yes.
"""

DIAG_UP = (-1,1)
DIAG_DOWN = (1,-1)
RIGHT = (0,1)
DOWN = (1,0)
POSSIBLE_MOVEMENTS = {
    DIAG_UP,
    DIAG_DOWN,
    RIGHT,
    DOWN
}
POSSIBLE_MOVEMENTS_DICT = {
    DIAG_UP : "DIAG_UP",
    DIAG_DOWN : "DIAG_DOWN",
    RIGHT : "RIGHT",
    DOWN : "DOWN",
}

class Buffer:
    def __init__(
        self,
        direction : str = "",
        buffer : "Buffer" = None,
    ):
        """
        Creates a 2 buffer
        """
        self.buffer = buffer
        self.direction =  direction
        
    def update(self, direction):
        if self.buffer is not None:
            self.buffer.update(self.direction)
        self.direction = direction
    
    def get_direction(self):
        print(self.direction)
        return self.direction

def boundary_check(limits : tuple, coords : tuple) -> bool:
    """
    limits is supposed to be unpacked as x_low, x_high, y_low, y_high
    coords is supposed to be unpacked as x,y
    """
    xl,xh,yl,yh = limits
    x,y = coords
    bound_x = xl <= x and x < xh
    bound_y = yl <= y and y < yh
    return bound_x and bound_y

def create_movement(coords : tuple , direction : tuple) -> tuple:
    x,y = coords
    xu,yu = direction
    return (
        x + xu,
        y + yu,
    )

def get_possible_movements(limits : tuple, coords : tuple) -> set:
    doable_movements = set()
    for possible_movement in POSSIBLE_MOVEMENTS:
        movement = create_movement(coords,possible_movement)
        if boundary_check(limits,movement):
            doable_movements.add(possible_movement)    
    return doable_movements
        

class Solution:
    def __init__(self):
        self.buffer2 = Buffer()
        self.buffer1 = Buffer("DIAG_UP",self.buffer2)
        
    def _get_next_movement(self,limits : tuple, coords : tuple):
        doable_movements = get_possible_movements(limits, coords)
        if len(doable_movements) == 1:
            return list(doable_movements)[0]
        
        if self.buffer1.get_direction() == "DIAG_UP":
            if RIGHT in doable_movements:
                self.buffer1.update(POSSIBLE_MOVEMENTS_DICT.get(RIGHT))
                return RIGHT
            elif DOWN in doable_movements:
                self.buffer1.update(POSSIBLE_MOVEMENTS_DICT.get(DOWN))
                return DOWN
        elif self.buffer1.get_direction() == "DIAG_DOWN":
            if DOWN in doable_movements:
                self.buffer1.update(POSSIBLE_MOVEMENTS_DICT.get(DOWN))
                return DOWN
            elif RIGHT in doable_movements:
                self.buffer1.update(POSSIBLE_MOVEMENTS_DICT.get(RIGHT))
                return RIGHT
        
        if self.buffer1.get_direction() == "RIGHT":
            if DIAG_DOWN in doable_movements:
                self.buffer1.update(POSSIBLE_MOVEMENTS_DICT.get(DIAG_DOWN))
                return DIAG_DOWN
            elif DIAG_UP in doable_movements:
                self.buffer1.update(POSSIBLE_MOVEMENTS_DICT.get(DIAG_UP))
                return DIAG_UP
        elif self.buffer1.get_direction() == "DOWN":
            if DIAG_UP in doable_movements:
                self.buffer1.update(POSSIBLE_MOVEMENTS_DICT.get(DIAG_UP))
                return DIAG_UP
            elif DIAG_DOWN in doable_movements:
                self.buffer1.update(POSSIBLE_MOVEMENTS_DICT.get(DIAG_DOWN))
                return DIAG_DOWN
        
    def _execute_movement(self, coords : tuple, movement : tuple, array : list, mat : list,limits : tuple) -> None:
        new_coords = create_movement(coords, movement)
        array.append(mat[new_coords[0]][new_coords[1]])
        while movement in {DIAG_UP,DIAG_DOWN} and boundary_check(limits,create_movement(new_coords, movement)):
            new_coords = create_movement(new_coords, movement)
            array.append(mat[new_coords[0]][new_coords[1]])
        return new_coords
                
            
    def findDiagonalOrder(self, mat: list) -> list:
        limits = (0,len(mat),0,len(mat[0]))
        coords = (0,0)
        upper_limit = (len(mat)-1,len(mat[0])-1)
        diagonal_order = []
        if mat is not [[]]:
            diagonal_order.append(mat[coords[0]][coords[1]])
        while upper_limit != coords:
            mvmt = self._get_next_movement(limits , coords )
            coords = self._execute_movement(coords,mvmt, diagonal_order, mat,limits)
        return diagonal_order
                
    
                
    
solution = Solution()
mat = [[1,2,3,12],[4,5,6,11],[7,8,9,10]]
res = solution.findDiagonalOrder(mat)