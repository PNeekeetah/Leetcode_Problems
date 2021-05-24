# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:22:35 2021

@author: Nikita
"""
"""
Manged to solve this under 8 minutes. I messed up the first time around 
because I misunderstood what was needed.

Beats 6.2 in terms of runtime and literally none in terms of memory because
I am storing 389 MB worth of data. OH WELL. I am using the Sieve of 
Eratosthenes to solve this.

"""

class Solution:
    def countPrimes(self, n: int) -> int:
        non_primes = dict()
        non_primes[1] = 1
        primes = dict()
        for i in range (1,n):
            if i in non_primes:
                continue
            else:
                primes[i] = 1
                for j in range (0,n,i):
                    non_primes[j] = 1
        return len(primes)
        
            
        