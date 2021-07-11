"""
Beats 91% in terms of runtime and
0% in terms of memory. 

First time submission succesful.
Took me 47:38 minutes to solve this.
"""


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        bits = bin(n//2)
        powers_of_20 = dict()
        powers_of_20[1] = 20
        MODULO = 10**9+7

        for i in range(2, len(bits)+1):
            powers_of_20[i] = powers_of_20[i-1]**2 % MODULO

        bits = list([bit for bit in bits])
        bits.reverse()
        bits = "".join(bits)
        number = 1

        for i, bit in enumerate(bits):
            if bit == "1":
                number = (number * powers_of_20[i+1]) % MODULO

        return (number*5**(n % 2)) % MODULO
