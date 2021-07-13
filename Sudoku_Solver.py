from typing import List, Dict, Set, Tuple

"""
Beats 50% in terms of runtime
Beats 30% in terms of memory usage 

It probably took me around 2 hours to
code this, but debugging it was  quite 
easy ( as opposed to some other problems 
I worked on).

First submission was succesful
This was labelled as hard.
"""

"""
For the moment, I just added methods for creating all the
sets  i'll need. I also added an occupied dict.

The idea is to write a backtracking algorithm that traverses the matrix
left to right, top to bottom.

The indices are passed as function parameters.


"""

NUMBERS = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def get_region(roc: int):
    """
    roc - row or column
    """
    region = (
        (0 <= roc and roc < 3)*0 +
        (3 <= roc and roc < 6)*1 +
        (6 <= roc and roc < 9)*2
    )
    return region


def get_square(row: int, col: int):
    sqr_row = get_region(row)
    sqr_col = get_region(col)
    return 3*sqr_row + sqr_col


def get_row_square_and_column(row: int, col: int, sets: List[List[Set[int]]]) -> Tuple[Set[int], Set[int], Set[int]]:
    """
    Gets the column, row and square sets
    corresponding to the given row and column
    """
    try:
        row_set = sets[0][row]
    except IndexError as e:
        print(row)
        print(e)
        raise
    col_set = sets[1][col]
    sqr_set = sets[2][get_square(row, col)]
    return (row_set, col_set, sqr_set)


def build_seen_sets(
    sets: List[List[Set[int]]],
    matrix: List[List[str]],
    occupied_dict: Dict[Tuple[int, int], bool]
):
    """
    Build a set of all seen numbers
    for each row, column and square
    """
    for row in range(9):
        for col in range(9):
            number = matrix[row][col]
            if number != ".":
                (row_set, col_set, sqr_set) = get_row_square_and_column(
                    row,
                    col,
                    sets
                )
                row_set.add(int(number))
                col_set.add(int(number))
                sqr_set.add(int(number))
                occupied_dict[(row, col)] = True


def get_available_numbers(row: int, col: int, sets: List[List[Set[int]]]) -> Set[int]:
    (
        row_set,
        col_set,
        sqr_set
    ) = get_row_square_and_column(
        row,
        col,
        sets
    )
    not_available = row_set.union(col_set)
    not_available = sqr_set.union(not_available)
    return NUMBERS - not_available


def add_num_to_sets(
    num: str,
    row: int,
    col: int,
    sets: List[List[Set[int]]]
) -> None:
    (
        row_set,
        col_set,
        sqr_set
    ) = get_row_square_and_column(
        row,
        col,
        sets
    )
    row_set.add(int(num))
    col_set.add(int(num))
    sqr_set.add(int(num))


def remove_num_from_sets(num: str, row: int, col: int, sets: List[List[Set[int]]]) -> None:
    (
        row_set,
        col_set,
        sqr_set
    ) = get_row_square_and_column(
        row,
        col,
        sets
    )
    row_set.remove(int(num))
    col_set.remove(int(num))
    sqr_set.remove(int(num))


def traverse(
    row: int,
    column: int,
    sets: List[List[Set[int]]],
    matrix: List[List[str]],
    occupied_dict: Dict[Tuple[int, int], bool]
):
    next_row = row
    next_col = column + 1
    if column == 8:
        next_row = row + 1
        next_col = 0

    if occupied_dict.get((row, column)) is not None:
        if row == 8 and column == 8:
            return True
        return traverse(next_row, next_col, sets, matrix, occupied_dict)

    numbers = get_available_numbers(row, column, sets)
    for number in numbers:
        add_num_to_sets(str(number), row, column, sets)
        if row == 8 and column == 8:
            matrix[row][column] = str(number)
            return True
        if traverse(next_row, next_col, sets, matrix, occupied_dict):
            matrix[row][column] = str(number)
            return True
        remove_num_from_sets(str(number), row, column, sets)
    return False


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        columns_sets_list: List[Set[int]] = [set() for _ in range(9)]
        rows_sets_list: List[Set[int]] = [set() for _ in range(9)]
        squares_sets_list: List[Set[int]] = [set() for _ in range(9)]
        sets = [rows_sets_list, columns_sets_list, squares_sets_list]
        occupied_spaces: Dict[Tuple[int, int], bool] = dict()
        build_seen_sets(sets, board, occupied_spaces)
        traverse(0, 0, sets, board, occupied_spaces)


solution = Solution()
board = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "8", ".", "6"]
]

solution.solveSudoku(board)
for l in board:
    print(l)
