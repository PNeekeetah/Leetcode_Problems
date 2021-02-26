class Solution:
    def __init__(self):
        self.solutions = 0
        return None
    
    def combo (self,numbers : list, target : int,dictionary : dict):
        if dictionary and (dictionary.get(target) != None) :
            self.solutions += dictionary.get(target) 
            return self.solutions
        if (target == 0):
            self.solutions += 1
            return
        elif(target < 0 ):
            return
        elif(target > 0):
            for number in numbers:
                self.combo(numbers, target - number,dictionary)
        return self.solutions

    def helper(self,numbers, target, dictionary = None):
        if not(dictionary):
            dictionary = {}
        if not(dictionary.get(target)):
            dictionary[target] = self.combo(numbers,target,dictionary)
        return dictionary

    def combinationSum4(self, nums: list, target: int) -> int:
        dictionary = {}
        for i in range(1,target + 1):
            self.solutions = 0
            dictionary = self.helper(nums,i, dictionary)
            
        self.solutions

"""
I submitted the solution above after 4 hours, 59 minutes and 50 seconds.

Submission worked on the first try. I had to resist the urge to look at the
solutions. I resisted succesfully. 

In terms of runtime, it beats 8 % of all the solutions BUT it beats 64%
in terms of memory usage (so my solution is actually quite light, to make up
for the terrible runtime).

The idea is to build the solution from the bottom up. First, find the solution
if the target is 1; add how many solutions exist in a dictionary. Work your
way up to the actual target.

In the recursive calls, if the solution was already found, you add the 
total number of solutions and then return.

If this [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
is the list and 12 is the target, the non optimized version makes
24577 calls. The optimized one makes 156. Above is the optimized version which
was submitted. The number of calls was reduced by a factor of 157!

Below, if "combo" is called by itself, it runs unoptimized. If "helper" is 
called, then the number of calls is reduced.

"""
solutions = 0
calls = 0

def combo (numbers : list, target : int,dictionary : dict):
    global solutions
    global calls
    calls += 1
    if dictionary and (dictionary.get(target) != None) :
        solutions += dictionary.get(target) 
        return solutions
    if (target == 0):
        solutions += 1
        return
    elif(target < 0 ):
        return
    elif(target > 0):
        for number in numbers:
            combo(numbers, target - number,dictionary)
    return solutions

def helper(numbers, target, dictionary = None):
    if not(dictionary):
        dictionary = {}
    if not(dictionary.get(target)):
        dictionary[target] = combo(numbers,target,dictionary)
    return dictionary

nums = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 12

combo (nums,target,None)

calls = 0
dictionary = {}
for i in range(1,target + 1):
    solutions = 0
    dictionary = helper(nums,i, dictionary)
    
