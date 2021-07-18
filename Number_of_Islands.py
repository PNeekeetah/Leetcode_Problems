"""
Took me about 20 minutes to come up with this
and debug it.

Solution beats 7.33 in terms of runtime and 18%
in terms of memory.
First time submission succesful
"""

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DELTAS = [UP, DOWN, LEFT, RIGHT]

Coords = Tuple[int, int]
Size = Tuple[int, int]


def transition(position: Coords, delta: Coords) -> Coords:
    return (
        position[0] + delta[0],
        position[1] + delta[1]
    )


def check_bounds(position: Coords, size: Size) -> bool:
    check_x = 0 <= position[0] and position[0] < size[0]
    check_y = 0 <= position[1] and position[1] < size[1]
    return check_x and check_y


def get_possible_positions(position: Coords, size: Size):
    possible_positions = []
    for delta in DELTAS:
        new_position = transition(position, delta)
        if check_bounds(new_position, size):
            possible_positions.append(new_position)
    return possible_positions


def is_land(grid: List[List[int]], position: Coords) -> bool:
    x, y = position
    return int(grid[x][y]) == 1


def explore_land(grid: List[List[int]], position: Coords, size: Size):
    land_list = [position]
    seen_land = {position}
    index = 0
    while index < len(land_list):
        explorable = get_possible_positions(land_list[index], size)
        for p in explorable:
            if is_land(grid, p) and p not in seen_land:
                land_list.append(p)
                seen_land.add(p)
        index += 1
    return land_list


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        position: Coords = (0, 0)
        size: Size = (len(grid), len(grid[0]))
        islands = []
        seen_land = set()
        for x in range(size[0]):
            for y in range(size[1]):
                il = is_land(grid, (x, y))
                if il and (x, y) not in seen_land:
                    land = explore_land(grid, (x, y), size)
                    seen_land = seen_land.union(set(land))
                    islands.append(land)
        return len(islands)
