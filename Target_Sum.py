from typing import List, Tuple

"""
Beats 26% in terms of runtime and 55 % in terms of memory.

This took me a couple of days of intense thinking. First
submission was not succesful since it went over the time
limit. (I tried submitting a pure backtracking solution).
"""

NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TARGET = 55


def dp(s, index, TARGET, NUMS, SUMS = None):
    if SUMS == None:
        SUMS = [[None for _ in range(-sum(NUMS),+sum(NUMS) + 1)] for _ in range(len(NUMS))]

    if s == TARGET and index == len(NUMS):
        return 1
    
    if index == len(NUMS):
        return 0
    
    if SUMS[index][s] is not None:
        return SUMS[index][s]
    
    else:
        p = rec3(s + NUMS[index], index + 1, TARGET, NUMS, SUMS)
        m = rec3(s - NUMS[index], index + 1, TARGET, NUMS, SUMS)
        SUMS[index][s] = p + m
        return p + m

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return dp(0,0,target,nums)




"""
First solution is a brute force approach.
It fails Leetcode's time limit.

Interestingly, the list comprehension one
which has only 1 branch is even slower 
than a normal for loop.
"""
NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TARGET = 3
TOTAL = 0
SEEN_DICT = dict()
CALLS = 0


def switch_symbols(symbols):
    return "".join(["-" if s == "+" else "+" for s in symbols])


def rec(accumulator, index, symbols):
    global NUMS, TARGET, TOTAL, CALLS, SEEN_DICT
    CALLS += 1
    SEEN_DICT[symbols] = accumulator
    switch = switch_symbols(symbols)
    SEEN_DICT[switch] = - accumulator

    if index == len(NUMS):
        TOTAL += (accumulator == TARGET) + (-accumulator == TARGET)
        return

    if SEEN_DICT.get(symbols + "+"):
        pass
    else:
        rec(accumulator + NUMS[index], index + 1, symbols + "+")

    if SEEN_DICT.get(symbols + "-"):
        pass
    else:
        rec(accumulator - NUMS[index], index + 1, symbols + "-")


#rec(0, 0, "")
#print(TOTAL, "It took {} calls to find this answer".format(CALLS))

"""
Split into 2 sets. + set and - set.
p_set - m_set = target 
p_set + m_set - 2*m_set = target 
SUM - 2*m_set = target
2*p_set - SUM = target 
2*p_set = SUM + target
p_set = (SUM + target)/2 

if index == length: 
    return 0

if seen[index][weight] is not None: 
    return seen[index][weight]

if acc_w + weight[index] > allowed_weight: 
    return rec(index+1, weight)

else:
    take = value[i] + rec(index+1,weight - weight[i])
    skip = rec(index+1,weight)
    best = max(take,skip)
    seen[index][weight] = best
    return best


"""


INDEX = int
SUM = int
value = (int(TARGET) + sum(NUMS))//2

TOTAL = 0


def dp_target_sum(index, target):
    global TARGET, TOTAL, NUMS, SUMS, value

    if target == 0:
        TOTAL += 1
        return value

    if index == len(NUMS):
        return value - target

    if SUMS[index][target] is not None:
        return SUMS[index][target]

    if target - NUMS[index] < 0:
        return dp_target_sum(index + 1, target)

    else:
        take = NUMS[index] + dp_target_sum(index + 1, target - NUMS[index])
        skip = dp_target_sum(index + 1, target)
        best = min(take, skip)
        SUMS[index][target] = best
        return best


#dp_target_sum(0, value)

# for l in SUMS:
#    for i in l:
#        TOTAL += (i == 1)

# print(TOTAL)

SUMS = []
if (TARGET + sum(NUMS)) % 2 != 1:
    SUMS = [[0 for _ in range(value+1)] for _ in range(len(NUMS)+1)]


def rec2(index, target):
    global NUMS, TOTAL, SUMS, TARGET

    if (TARGET + sum(NUMS)) % 2 == 1:
        return 0

    if target == 0:
        return 1

    if index == len(NUMS):
        return 0

    if target - NUMS[index] < 0:
        return rec2(index+1, target)

    else:
        i1 = rec2(index+1, target - NUMS[index])
        i2 = rec2(index+1, target)
        SUMS[index][target] += max(i1, i2)
        return max(i1, i2)

SUMS = [[None for _ in range(-sum(NUMS),+sum(NUMS) + 1)] for _ in range(len(NUMS))]
CALLS = 0
def rec3(sum, index):
    global NUMS, TARGET, CALLS
    CALLS += 1 
    if sum == TARGET and index == len(NUMS):
        return 1
    
    if index == len(NUMS):
        return 0
    
    if SUMS[index][sum] is not None:
        return SUMS[index][sum]
    else:
        p = rec3(sum + NUMS[index], index + 1)
        m = rec3(sum - NUMS[index], index + 1)
        SUMS[index][sum] = p + m
        return p + m

val = rec3(0,0)
print(val)
print(CALLS)


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        template = "{number:0>{length}}"
        num_template = "{0}{1}"
        total = 0

        for i in range(2**length):
            symbols = template.format(number=bin(i)[2:], length=length)
            accumulator = sum(
                [
                    int(
                        num_template.format(
                            ("+" if s == "1" else "-"),
                            num
                        )
                    ) for s, num in zip(symbols, nums)
                ]
            )
            total += accumulator == target

        return total


sol = Solution()
print(sol.findTargetSumWays(NUMS, TARGET))
