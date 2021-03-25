# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:22:00 2021

@author: Nikita
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: list(), k: int) -> int:
        window = 1
        start = 0
        product = nums[start]
        solutions = 0
        while start + window < len(nums):
            while product < k and start + window < len(nums):
                solutions += window*(product < k)
                product *= nums[start + window]
                window += 1
            product /= nums[start]
            start += 1
            window -= 1
        if (product < k):
            solutions += window + (window > 1)
        
        return solutions
    
    def numSubarrayProductLessThanK1(self, nums, k): # Copied solution from leetcode
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
    
solution = Solution()
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [10,2,5,6]
he = solution.numSubarrayProductLessThanK(l2,20)
        
        
solution = Solution()
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [10,2,5,6]
he = solution.numSubarrayProductLessThanK(l1,20)


"""
After 4 hours and 3 minuts, I give up. Conceptually, I know how to solve the 
problem. Practically, I cannot code it. It's useless to try to debug any further.


# Marks the starting index
1,2,3,4,5,6,7,8,9,10        20
#                       WIN = 1, SOL = 1, PROD = 1 < 20
# #                     WIN = 2, SOL = 3, PROD = 2 < 20
# # #                   WIN = 3, SOL = 6, PROD = 6 < 20
# # # #                 WIN = 4, SOL = 6, PROD = 24 > 20
  # # #                 WIN = 3, SOL = 6, PROD = 24 > 20
    # #                 WIN = 2, SOL = 8, PROD = 12 < 20
    # # #               WIN = 3, SOL = 8, PROD = 60 > 20
      # #               WIN = 2, SOL = 8, PROD = 20 >= 20
        #               WIN = 1, SOL = 9, PROD = 5  < 20
        # #             WIN = 2, SOL = 9, PROD = 30 > 20
          #             WIN = 1, SOL = 10, PROD = 6 < 20
          # #           WIN = 2, SOL = 10, PROD = 42 > 20
            #           WIN = 1, SOL = 11, PROD = 7 < 20
            # #         WIN = 2, SOL = 11, PROD = 56 > 20
              #         WIN = 1, SOL = 12, PROD = 8 < 20
              # #       WIN = 2, SOL = 12, PROD = 72 > 20
                #       WIN = 1, SOL = 13, PROD = 9 < 20
                # #     WIN = 2, SOL = 13, PROD = 90 > 20
                  #     WIN = 1, SOL = 14, PROD = 10 < 20
                  # #   WIN = 2, SOL = 14, START + WIN >= LEN(NUMS) -> RETURN 14

10, 5, 2, 6                 100
#                       WIN = 1, SOL = 1, PROD = 10
#   #                   WIN = 2, SOL = 3, PROD = 50
#   #  #                WIN = 3, SOL = 3, PROD = 100
    #  #                WIN = 2, SOL = 5, PROD = 10
    #  #  #             WIN = 3, SOL = 8, PROD = 60
    #  #  #  #          WIN = 4, SOL = 8, START + WIN > LEN(NUMS) -> RETURN 8


"""