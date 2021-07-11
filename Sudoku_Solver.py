from typing import List, Dict, Set, Tuple

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
    row_set = sets[0][row]
    col_set = sets[1][col]
    sqr_set = sets[2][get_square(row, col)]
    return (row_set, col_set, sqr_set)


def build_seen_sets(sets: List[List[Set[int]]], matrix: List[List[str]], occupied_dict: Dict[Tuple[int, int], bool]):
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
                row_set.add(number)
                col_set.add(number)
                sqr_set.add(number)
                occupied_dict[(row, col)] = True


def get_available_numbers(row: int, col: int, sets: List[List[Set[int]]]) -> set:
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


def add_num_to_sets(num: int, row: int, col: int, sets: List[List[Set[int]]]) -> None:
    (
        row_set,
        col_set,
        sqr_set
    ) = get_row_square_and_column(
        row,
        col,
        sets
    )
    row_set.add(num)
    col_set.add(num)
    sqr_set.add(num)


def remove_num_from_sets(num: int, row: int, col: int, sets: List[List[Set[int]]]) -> None:
    (
        row_set,
        col_set,
        sqr_set
    ) = get_row_square_and_column(
        row,
        col,
        sets
    )
    row_set.remove(num)
    col_set.remove(num)
    sqr_set.remove(num)


def traverse(row: int, column: int, sets: List[List[Set[int]]], matrix: List[List[str]]):
    pass


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        columns_sets_list: List[Set[int]] = [set() for _ in range(9)]
        rows_sets_list: List[Set[int]] = [set() for _ in range(9)]
        squares_sets_list: List[Set[int]] = [set() for _ in range(9)]
        sets = [rows_sets_list, columns_sets_list, squares_sets_list]
        occupied_spaces = dict()
        build_seen_sets(sets, board, occupied_spaces)
