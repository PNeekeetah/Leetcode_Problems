from typing import List

"""
Took me about 30 minutes to figure this out.
Solution beats 35 in terms of runtime and 22%
in terms of memory usage. 

First time submission successful.

"""


def recursive_combine(
    k: int,
    nums_list: List[int],
    partial_solution: List[int] = None,
    all_solutions: List[List[int]] = None,
) -> List[List[int]]:

    if partial_solution is None:
        partial_solution = list()

    if all_solutions is None:
        all_solutions = list()

    if k == 0:
        all_solutions.append(list(partial_solution))
        return

    list_length = len(nums_list)

    while list_length > 0:
        num = nums_list.pop()
        partial_solution.append(num)
        recursive_combine(k-1, list(nums_list),
                          partial_solution, all_solutions)
        list_length = len(nums_list)
        partial_solution.pop()

    return all_solutions


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        available_numbers = [_ for _ in range(n, 0, -1)]
        all_solutions = recursive_combine(k, available_numbers)
        return all_solutions
