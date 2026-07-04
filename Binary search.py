from typing import List


nums = [3, 5, 7, 9, 11]
target = 11


def search( nums: List[int], target: int) -> int:

    left , right = 0 , len(nums) - 1

    while left <= right :
        mid = (left + right) // 2

        if nums[mid] == target :
            return mid
        elif nums[mid] < target :
             left = mid + 1
        else :
            right = mid - 1

    
    return -1

result = search(nums,target)

print(result)
