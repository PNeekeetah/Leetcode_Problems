# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:38:39 2020

@author: Nikita
"""

import AccurateTime
from BenchmarkSuite import *

def convertToList (string : str) -> list:
    """
    Parameters
    ----------
    string : str
        String represents the text input.

    Returns
    -------
    list
        Returns a list.
    """
    characterList = []
    for char in string:
        characterList.append(char)
    return characterList

class Solution(object):
    
    def __init__(self):
        None;
    
    def reverseString(self, s : list) -> None:
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        end = len(s) - 1
        aux = "0"
        for i in range ((end + 1)//2):
            aux = s[end]
            s[end] = s[i]
            s[i] = aux
            end -= 1
    
    def reverseStringOneLiner1(self, s : list) -> None:
        s.reverse()
        
    def reverseStringOneLiner2(self, s : list) -> None:
        s = s.reverse()
            
def main():
    string = """Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng]velit, sed quia non numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum[d] exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur? [33] At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat…"""
    toList = convertToList(string)
    solution = Solution()
    trials = 10**3
    benchmark(solution.reverseString, trials, import_name = "Reverse_String",
              obj = solution, self = "obj", s = toList)

if __name__ == "__main__":
    main()
