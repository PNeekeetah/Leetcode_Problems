# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:44:12 2021

@author: Nikita
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if (n == 0):
            return 0
        non_primes = {0 : 1, 1 : 1}
        for i in range(2,n+1,1):
            if not(non_primes.get(i)):
                multiple = 2
                target = multiple*i
                while (target <= n):
                    non_primes[target] = 1
                    multiple += 1
                    target = multiple*i
        values = list(non_primes.keys())
        values.sort()
        return values
                    
            
solution = Solution()
dictionary = solution.countPrimes(5*10**6)
all_entries = {}
current_nonprime = 0
primes = 0
for i in range (0,5*10**6):
    if (dictionary[current_nonprime] == i):
        all_entries[i] = primes
        current_nonprime += 1
    else:
        primes += 1
        all_entries[i] = primes
        
f = open("PrimeDictionary","w")
f.write(str(all_entries))
f.close()

while (1):
    print("Request a number, I will tell you how many primes exist up to that point.")
    n = input()
    print("There are {} primes up until {}.".format(all_entries[n],n))