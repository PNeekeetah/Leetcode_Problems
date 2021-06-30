# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:03:41 2021

@author: Nikita
"""

"""
Beats 82 % in terms of runtime and 
14% in terms of memory usage. 

Second submission was succesful because 
I messed up the initial minimum index / 
I didn't take into account that the maximum
of one list can be smaller  than the sum of 2
indices of both.
"""

def create_restaurant_index_dict(restaurants : list) -> dict:
    favourite_restaurants = dict()
    for index,restaurant in enumerate(restaurants):
        favourite_restaurants[restaurant] = index
    return favourite_restaurants

class Solution:
    def findRestaurant(self, list1: list, list2: list) -> list:
        favourite_restaurants1 = create_restaurant_index_dict(list1)
        favourite_restaurants2 = create_restaurant_index_dict(list2)
        common_restaurants = set(list1).intersection(set(list2))
        min_index =len(list1)+len(list2)+1
        index_listings = dict()
        for common in common_restaurants:
            index_sum = favourite_restaurants1[common] + favourite_restaurants2[common]
            if index_sum < min_index:
                min_index = index_sum
            
            index_listings.setdefault(index_sum,[]).append(common)
            
            
        return index_listings[min_index]