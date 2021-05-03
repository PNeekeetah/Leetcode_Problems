# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 14:39:18 2021

@author: Nikita
"""

"""
After 29 minutes and 40 seconds, I gave up.

First solution works, but it fails when it comes to the time limit.

I got the second solution after reading my friend's code. Although 
the submission was successful, I gave up.
"""

class Solution:
    def getWinner(self, arr: list, k: int) -> int:          #first solution
        dictionary = {
            elem : 0 
            for elem in arr
        }
        to_win = k
        winner = arr[0]
        array_elements = len(arr) - 2
        maximum = max(arr[0],arr[1])
        while True:
            if arr[0] > arr[1]:
                dictionary[arr[0]] += 1
                dictionary[arr[1]] = 0
                last = arr.pop(1)
                arr.append(last)
            else:
                dictionary[arr[1]] += 1
                dictionary[arr[0]] = 0
                last = arr.pop(0)
                arr.append(last)
            if arr[0] > maximum:
                    maximum = arr[0]
                    array_elements -= 1
                    if array_elements == 0:
                        winner = maximum
                        break
            if dictionary[arr[0]] == k:
                winner = arr[0]
                break
        return winner
        
            
    def getWinner1(self, arr: list, k: int) -> int: #second solution
        winner = arr[0]
        wins = 0
        for i in range(1,len(arr)):
            if winner > arr[i]:
                wins += 1
            else:
                winner = arr[i]
                wins = 1 
            if wins == k:
                break
        return winner
            