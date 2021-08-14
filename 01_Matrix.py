from typing import List

DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]

def bound_check(coords, size):
    x_check = 0 <= coords[0] and coords[0] < size[0]
    y_check = 0 <= coords[1] and coords[1] < size[1]
    return x_check and y_check


def find_closest_zero(origin, matrix, seen_zeroes):
    global DIRECTIONS
    
    queue = [(origin, 0)]
    seen = {origin}
    index = 0
    size = (len(matrix),len(matrix[0]))
    distance = 0
    current = None
    
    while index < len(queue):
        current, distance = queue[index]
        
        if matrix[current[0]][current[1]] == 0 or seen_zeroes.get(current) is not None:
            print("Broke after {} iterations".format(index))
            break
                
        for d in DIRECTIONS:
            new_coord = (current[0] + d[0], current[1] + d[1])
            if bound_check(new_coord, size) and new_coord not in seen:
                queue.append((new_coord,distance + 1))
                seen.add(new_coord)
        
        index += 1
    
    if seen_zeroes.get(current) is not None:
        seen_zeroes[origin] = seen_zeroes.get(current) - distance
        return seen_zeroes[origin]
    
    seen_zeroes[origin] = distance
    
    return distance

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        new_matrix = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        seen_zeroes = dict()
        for i in range (len(mat)):
            for j in range (len(mat[0])):
                coords = (i,j)
                new_matrix[i][j] = find_closest_zero(coords, mat, seen_zeroes)
        return new_matrix
        
        
import random 
matrix = [[random.choice([0,1]) for _ in range(10)] for _ in range(10)]

solution = Solution()
val = solution.updateMatrix([[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1]])
print(val)
print(matrix)