"""
Took me about 25 minutes to solve.

Beats 94 % in terms of runtime and 
35% in terms of memory usage.

First time submission succesful.
"""


class Solution:
    def sortString(self, s: str) -> str:
        # Create the characters dictionary
        chars_dict = dict()
        for char in s:
            chars_dict.setdefault(char, 0)
            chars_dict[char] += 1

        # Create the new string and start by ascending
        new_string = ""
        letters = list(chars_dict.keys())
        ascend = True

        while len(letters) > 0:
            # Sort the letters and reverse them if descending
            letters.sort()
            if ascend != True:
                letters.reverse()

            # Add letters to string and delete them as necessary
            for letter in letters:
                new_string += letter
                chars_dict[letter] -= 1
                if chars_dict[letter] == 0:
                    chars_dict.pop(letter)

            # Get the remaining letters and switch modus operandi
            letters = list(chars_dict.keys())
            ascend = ascend ^ True

        return new_string
