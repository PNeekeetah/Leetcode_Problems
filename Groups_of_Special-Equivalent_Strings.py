"""
Beats 17% in terms for runtime
Beats 69% in terms of memory requirements

First time submission, took me 20 minutes and 
30 seconds to submit.
"""


def build_key(odd_dict, evn_dict, alphabet):
    odd_repr = ""
    evn_repr = ""
    for letter in alphabet:
        if odd_dict.get(letter) is not None:
            odd_repr += letter + str(odd_dict[letter])
        if evn_dict.get(letter) is not None:
            evn_repr += letter + str(evn_dict[letter])
    result = evn_repr + odd_repr
    return result


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        odd_letters_dict = dict()
        evn_letters_dict = dict()
        all_letters = "abcdefghijklmnopqrstuvwxyz"
        all_sets = set()
        for word in words:
            for index, letter in enumerate(word):
                if index % 2 == 0:
                    evn_letters_dict.setdefault(letter, 0)
                    evn_letters_dict[letter] += 1
                else:
                    odd_letters_dict.setdefault(letter, 0)
                    odd_letters_dict[letter] += 1

            all_sets.add(build_key(odd_letters_dict,
                         evn_letters_dict, all_letters))
            odd_letters_dict = dict()
            evn_letters_dict = dict()
        return len(all_sets)
