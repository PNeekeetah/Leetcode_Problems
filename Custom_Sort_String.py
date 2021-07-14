"""
Beats 100% in terms of runtime 
Beats 0 % in terms of memory 
First submission succesful
"""

class Solution:
    def customSortString(self, order: str, string: str) -> str:
        char_dict = {c:0 for c in order}
        top_half = ""
        bottom_half = ""

        for c in string:
            if char_dict.get(c) is not None:
                char_dict[c] += 1
            else:
                top_half += c

        for c in order:
            bottom_half = "".join(
                [
                    bottom_half,
                    "".join( 
                        [c for _ in range(char_dict[c]) ] 
                    )
                ]
            )

        bottom_half = "".join([bottom_half,top_half])
        
        return bottom_half