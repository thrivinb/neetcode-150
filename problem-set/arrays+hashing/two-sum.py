'''
Problem Statement: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

'''
Initial Thoughts

1. What are the constraints?
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.
    Do not use same element twice.

2. Since only one valid answer exists, we can early terminate if we find an answer.

3. If we can hash all we have visited, and check if current value's complement has been visited, we can solve this problem

    N = length of nums
    O(N) space -> to hash all visited values
    O(N) time -> In the worst case, N O(1) lookups will be made 
'''

def two_sum(nums, target):
    complement_map = dict()

    for i in range(0, len(nums)):
        num = nums[i]
        complement = target - num
        if num in complement_map:
            # match has been discovered, return indices of complement and current element
            return [complement_map.get(num), i]
        
        complement_map[complement] = i
    
    # In case no match
    return []
