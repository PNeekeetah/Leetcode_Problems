# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:10:28 2021

@author: Nikita
"""

"""
First time submission succesfull.
Took me about 40 minutes to code this.

It beats 85% in terms of runtime and
0 % in terms of memory.
"""

TRAVERSE_UP = (-1,0)
TRAVERSE_DOWN = (1,0)
TRAVERSE_LEFT = (0,-1)
TRAVERSE_RIGHT = (0,1)

TRAVERSE_NEXT = {
    TRAVERSE_RIGHT : TRAVERSE_DOWN,
    TRAVERSE_DOWN : TRAVERSE_LEFT,
    TRAVERSE_LEFT : TRAVERSE_UP,
    TRAVERSE_UP : TRAVERSE_RIGHT,
}

Limits = (int,int,int,int) 
Coords = (int,int)


def check_bound (next_coords : Coords, limits : Limits) -> bool:
    xl, xh, yl, yh = limits
    x,y = next_coords
    bound_x = xl <= x and x < xh
    bound_y = yl <= y and y < yh
    return bound_x and bound_y

def move (coords : Coords, direction : Coords) -> Coords:
    x,y = coords
    xu,yu = direction
    return (
        x + xu,
        y + yu,
    )

def get_next_direction (current_direction : Coords) -> Coords:
    return TRAVERSE_NEXT.get(current_direction)
        
class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        coords = (0,0)
        if mat == [[]]:
            return []
        value = mat[coords[0]][coords[1]]
        spiral_order = [value]
        limits = (0,len(mat), 0, len(mat[0]))
        direction = TRAVERSE_RIGHT
        squares_left = len(mat)*len(mat[0]) - 1
        explored = set()
        explored.add(coords)
        while squares_left > 0:
            tentative_coords = move(coords, direction)
            while check_bound(tentative_coords, limits) and tentative_coords not in explored:
                squares_left -= 1
                coords = tentative_coords
                explored.add(coords)
                value = mat[coords[0]][coords[1]]
                spiral_order.append(value)
                tentative_coords = move(coords, direction)
            else:
                direction = get_next_direction(direction)
                
        return spiral_order