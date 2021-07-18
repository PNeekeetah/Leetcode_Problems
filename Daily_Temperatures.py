from typing import List

"""
Beats 22% in terms of runtime and 0 %
in terms of memory. Likely due to the 
the usage of a dictionary , a stack and
a list comprehension at the end.

First submission succesful.
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Append temperature in a stack if it's lower than the top of the stack.
        Otherwise, pop all temperatures that are lower than the current one.

        """
        stack = list()
        days_temp_dict = dict()
        for index, temp in enumerate(temperatures):
            days_temp_dict[index] = 0
            while len(stack) > 0 and stack[-1][0] < temp:
                days_temp_dict[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
            else:
                stack.append((temp, index))

        return [days_temp_dict[i] for i in range(len(temperatures))]
