"""
Beats 93% in terms of runtime and 67%
in terms of memory usage.

First time submission succesful.

I just found out that -1//6 is not 0 
but actually -1/ this lead to an
alternative implementation of this
function.
"""


def op_plus(elem1: int, elem2: int):
    return elem1 + elem2


def op_mins(elem1: int, elem2: int):
    return elem1 - elem2


def op_mult(elem1: int, elem2: int):
    return elem1 * elem2


def op_divd(elem1: int, elem2: int):
    negatives = 0
    if elem1 < 0:
        negatives += 1
    if elem2 < 0:
        negatives += 1
    return abs(elem1) // abs(elem2) * (-1)**negatives


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = {
            "+": op_plus,
            "-": op_mins,
            "/": op_divd,
            "*": op_mult
        }
        stack = list()
        for tk in tokens:
            if tk in symbols:
                element2 = stack.pop()
                element1 = stack.pop()
                stack.append(symbols[tk](element1, element2))
            else:
                stack.append(int(tk))
        return stack[0]
