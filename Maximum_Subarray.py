"""
I actually have no clue how to solve this problem besides the O(n^2) method.
It's been 4 hours and 5 minutes of intense head scratching and nothing came
of it. I left the solution here. 

I will now go ahead and cheat and read the wikipedia article with regards
to the algorithm.  

I just copied the wikipedia code because I was getting tired. After 5 hours
and 16, I feel like this day would have been more productive if I knew 
how to give up earlier. I won't give any submission details since it's
not my own work.

The solution seems to be doing the following : 
    current_sum starts out as 0 
    if adding X to the current sum increases the number, current_sum is
    updated.
    if current_sum is larger than best sum, best_sum is updated with the
    current_sum
    
    best sum starts out as -2**31, the most negative 32 bit integer.
    

"""
l = [1,2,3,-60,-60, 1,3,4,300, -60,-60, 1,2,3, -60,-60,199]
#l = [-1*10**3,-2**2**2**2**2,-3**2**2**2,-199,-2*2**2**2**2]

def max_subarray(numbers):
    
    best_sum = -2**31
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

print(max_subarray(l))
