
from typing import List
from random import randint


def binary_search(nums: List[int], target: int) -> bool:
    start: int = 0
    end: int = len(nums) - 1
    while start <= end:
        middle = (start + end)//2
        if nums[middle] == target:
            return True
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return False


def binary_search_rotated(nums: List[int], target: int) -> bool:
    start: int = 0
    end: int = len(nums) - 1
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return True
        # Left part is sorted
        elif nums[start] <= nums[middle]:
            # and target is found in the left part
            if nums[start] <= target and target <= nums[middle]:
                return binary_search(nums[start:middle+1], target)
            else:
                start = middle + 1
        # Right part is sorted
        elif nums[middle] <= nums[end]:
            # and target is found in the right part (and bounded)
            if target >= nums[middle] and target <= nums[end]:
                return binary_search(nums[middle:end+1], target)
            else:
                end = middle - 1
    return False


def binary_search_rot(nums: List[int], start: int, end: int, target) -> bool:
    if start >= end:
        return False
    middle = (start + end)//2
    if nums[start] <= nums[middle] and nums[middle] <= nums[end]:
        return binary_search_rot(nums, start, middle-1, target) or binary_search_rot(nums, middle + 1, end, target)
    elif nums[start] <= nums[middle]:
        if nums[start] <= target and target <= nums[middle]:
            return binary_search(nums[start:middle+1], target)
        else:
            return binary_search_rot(nums, middle + 1, end, target)
    elif nums[middle] <= nums[end]:
        if nums[middle] <= target and target <= nums[end]:
            return binary_search(nums[middle:end+1], target)
        else:
            return binary_search_rot(nums, start, middle - 1, target)


def binary_search_rotated_2(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return True
        elif nums[start] < nums[middle] and nums[start] < target and target < nums[middle]:
            return binary_search(nums[start:middle+1], target)
        elif nums[middle] < nums[end] and nums[middle] < target and target < nums[end]:
            return binary_search(nums[middle:end+1], target)
        elif nums[start] < nums[middle] and nums[middle] < target:
            start = middle + 1
        elif nums[middle] < nums[end] and nums[middle] > target:
            end = middle - 1
        elif nums[start] == nums[middle] and nums[end] == nums[middle]:
            start += 1
        else:
            end -= 1


def binary_rot_search(nums: List[int], target: int) -> bool:
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = (start + end) // 2


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return binary_search_rotated_2(nums, target)


def rotate_array(array: List[int], rotation: int):
    temp: List[int] = array[-rotation:]
    temp.extend(array[:-rotation])
    return temp


array = [0, 0, 1, 2, 2, 5, 5, 5, 6]
#array = [5,6,7,8,0,1,2,3,4]
# print(array)

solution = Solution()
#val = solution.search(array,8)
for i in range(100):
    #array = [randint(0, 100) for _ in range(100)]
    # array.sort()
    #array = rotate_array(array, randint(0, 100))
    array = [1, 0, 1, 1, 1]
    try:
        assert (binary_search_rotated_2(array, 0) == (0 in array))
    except AssertionError as e:
        print(array)
        break
    print(i)
