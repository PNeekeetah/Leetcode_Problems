"""
Beats 65% in terms of runtime and 77% in terms of memory.

Second submission succesful because i forgot to add the
first time the original pixel to the explored set.

Took me 7 minutes to solve
"""
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]

def bound_check(coords, size):
    x_check = 0 <= coords[0] and coords[0] < size[0]
    y_check = 0 <= coords[1] and coords[1] < size[1]
    return x_check and y_check

def explore(start, matrix):
    global DIRECTIONS
    explored_set = set()
    explored_set.add(start)
    queue = [start]
    index = 0
    original_color = matrix[start[0]][start[1]]
    while index < len(queue):
        current = queue[index]
        tentative_set = []
        size = (len(matrix),len(matrix[0]))
        for d in DIRECTIONS:
            new_coord = (current[0] + d[0], current[1] + d[1])
            if (
                bound_check(new_coord, size) and 
                matrix[new_coord[0]][new_coord[1]] == original_color and 
                new_coord not in explored_set
            ):
                tentative_set.append(new_coord)
                explored_set.add(new_coord)
        queue.extend(tentative_set)
        index += 1
    
    return explored_set
                
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        origin = (sr,sc)
        adjacent = explore(origin, image)
        for a in adjacent:
            image[a[0]][a[1]] = newColor
        
        return image