"""
What I really like about this solution is the following : 
    
I spent 30 minutes trying to come up with a way to convert from 
arabic to roman, and then I realised that I was supposed to do
it the other way around. 

I was forced to flip the dictionary at the end of each function
because I was too lazy too rewrite it. 

Besides that, the solution "just works". I messed up a dict 
entry and I said "X" instead of "L" for 50 and I also 
introduced 1 more break statement than I needed.

Well, the runtime is terrible and the memory usage is terrible 
as well (see dict comprehension + the fact that I stick functions into
dicts)
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        
        def build_units(units_number : int) -> str:
            
            lookup = {
                1 : "I",
                2 : "II",
                3 : "III",
                4 : "IV",
                5 : "V",
                6 : "VI",
                7 : "VII",
                8 : "VIII",
                9 : "IX",
            }
            units = { 
                value : key 
                for key,value 
                in lookup.items()        
            }
            if units_number in units:
                return (True,units[units_number])
            else:
                return (False,"O")      
            
        def build_decimal (decimal_number : int) -> str:

            lookup = {
                10 : "X",
                20 : "XX",
                30 : "XXX",
                40 : "XL",
                50 : "L",
                60 : "LX",
                70 : "LXX",
                80 : "LXXX",
                90 : "XC",
            }
            decimal = { 
                value : key 
                for key,value 
                in lookup.items()        
            }
            if decimal_number in decimal:
                return (True,decimal[decimal_number])
            else:
                return (False,"O")
        
        def build_hundreds (hundreds_number : int) -> str:

            lookup = {
                100 : "C",
                200 : "CC",
                300 : "CCC",
                400 : "CD",
                500 : "D",
                600 : "DC",
                700 : "DCC",
                800 : "DCCC",
                900 : "CM",
            }
            hundreds = { 
                value : key 
                for key,value 
                in lookup.items()        
            }
            if hundreds_number in hundreds:
                return (True,hundreds[hundreds_number])
            else:
                return (False,"O")
        
        def build_thousands (thousands_number : str) -> (bool,int):
            
            lookup = {
                1000 : "M",
                2000 : "MM",
                3000 : "MMM",
            }
            thousands = { 
                value : key 
                for key,value 
                in lookup.items()        
            }
            if thousands_number in thousands:
                return (True,thousands[thousands_number])
            else:
                return (False,"O")
        
        def wrapper( number : str, modus : int) -> (bool,int):
            function_lookup = {
                0 : build_units,
                1 : build_decimal,
                2 : build_hundreds,
                3 : build_thousands,
            }
            return function_lookup[modus](number)
        
        roman_len = len(s) # 0 - len(s)-1 is the string or [0:len(s)]
        offset = 0
        accumulator = 0
        for modus in range (0,4):
            highest = 0
            start = None
            tentative_offset = 0
            for i in range (1,5):
                start = roman_len - i - offset
                if start < 0:
                    break
                end = roman_len - offset 
                success, number = wrapper(s[start:end],modus)
                if success:
                    highest = number
                    tentative_offset = i
            accumulator += highest
            offset += tentative_offset
        return accumulator
    
solution = Solution()
no = solution.romanToInt("III")