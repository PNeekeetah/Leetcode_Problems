from typing import List, Tuple, Dict

"""
Beats 6% in terms of runtime and 57% 
in terms of memory.

Took me quite a bit to solve this one.
The reason was a bug where I forgot
to delete the set of positions after
removing the queen from the board.

First time submission succesful.

This was apparently a hard one.

"""


UP = (-1, 0)
RIGHT_UP = (-1, 1)
RIGHT = (0, 1)
RIGHT_DOWN = (1, 1)
DOWN = (1, 0)
LEFT_DOWN = (1, -1)
LEFT = (0, -1)
LEFT_UP = (-1, -1)
DIRECTIONS = [UP, RIGHT_UP, RIGHT, RIGHT_DOWN, DOWN, LEFT_DOWN, LEFT, LEFT_UP]


def bound_check(position: Tuple[int, int], size: int):
    x_check = 0 <= position[0] and position[0] < size
    y_check = 0 <= position[1] and position[1] < size
    return x_check and y_check


class Queen:
    def __init__(self):
        self.positions: Tuple[int, int] = set()
        self.placed = False

    def place_queen(self, place: Tuple[int, int], board_dict: Dict[Tuple[int, int], int], board_size: int):
        if board_dict[place] != 0:
            return False

        for direction in DIRECTIONS:
            next_place = (
                place[0] + direction[0],
                place[1] + direction[1]
            )
            while bound_check(next_place, board_size):
                self.positions.add(next_place)
                board_dict[next_place] += 1
                next_place = (
                    next_place[0] + direction[0],
                    next_place[1] + direction[1]
                )
        self.positions.add(place)
        board_dict[place] += 1
        self.placed = True
        return True

    def remove_queen(self, board_dict):
        if len(self.positions) == 0:
            return False

        for position in self.positions:
            board_dict[position] -= 1

        self.positions = set()
        self.placed = False
        return True

    def is_placed(self):
        return self.placed


def create_board_dict(size: int) -> Dict[Tuple[int, int], int]:
    board_dict: Dict[Tuple[int, int]] = dict()
    for row in range(size):
        for col in range(size):
            board_dict[(row, col)] = 0
    return board_dict


def place_queens(row: int, queens: List["Queen"], board_dict: Dict[Tuple[int, int], int], size: int):
    ways = 0
    for col in range(size):
        if queens[row].place_queen((row, col), board_dict, size):
            if row == size - 1:
                ways += 1
            else:
                ways += place_queens(row+1, queens, board_dict, size)
            queens[row].remove_queen(board_dict)

    return ways


class Solution:
    def totalNQueens(self, n: int) -> int:
        queens = [Queen() for _ in range(n)]
        board_dict = create_board_dict(n)
        return place_queens(0, queens, board_dict, n)


solution = Solution()
print(solution.totalNQueens(9))
