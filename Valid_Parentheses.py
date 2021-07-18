"""
This problem took me 5 minutes to solve.
It beats 86% in terms of runtime and
63% in terms of memory usage.

My second submission was succesful because
I forgot to account for whether the stack
was empty at the end or not. The parantheses
are valid iff:
1. The first time one of {"}","]",")"} is encountered,
the very last stack item is the matching pair and
2. The stack should be empty at the end of the algorithm.

I am surprised I ended up thinking for 3 hours about this 
problem 3 weeks ago when It took me so little to solve
it today. 
"""


PAIRS = {
    ")": "(",
    "]": "[",
    "}": "{",
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for char in s:
            if char in {"(", "[", "{"}:
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == PAIRS[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
