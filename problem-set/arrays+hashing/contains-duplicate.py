''' 
Problem Statement: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''

'''
Initial Thoughts:

1. What are the constraints?
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9 

2. How space-constrained are we?
# If not, hashing would be most appropriate -> O(N) time complexity, O(N) space complexity

# If yes, use an O(1) space complexity sorting algo (e.g. Heap Sort) 
    and traverse resulting sorted array for duplicate check -> O(N log N) time complexity
'''

def is_contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    visited = set()

    for num in nums:
        if num in visited:
            # Duplicate detected, return True
            return True
        visited.add(num)

    # No duplicates detected, return False
    return False
  
            

