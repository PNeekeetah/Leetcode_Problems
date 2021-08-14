"""
Took me about 45 minutes to solve this 
Beats 45% in terms of Runtime and 87% in terms of 
memory usage.

4th time submission succesful. 

I noticed that the sum of all numbers modulo K must be 0
My friend noticed that the sum of each number modulo k all modulo k must be 0
This is how this solution came to be. 
"""
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        numbers_dict = {}
        for num in arr:
            key = num % k
            numbers_dict.setdefault(key, 0)
            numbers_dict[key] += 1

        for key in numbers_dict.keys():
            inverse = (k - key) % k

            if (
                numbers_dict.get(inverse) is None or 
                numbers_dict[key] != numbers_dict.get(inverse) or 
                inverse == key and numbers_dict[key]%2 == 1
               ):
                    return False

        return True
        
        
            