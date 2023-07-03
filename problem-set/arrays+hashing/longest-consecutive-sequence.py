'''
Problem Statement: https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

'''
Initial Thoughts

1. What are the constraints?
    0 <= nums.length <= 10^5
   -10^9 <= nums[i] <= 10^9

2. Approach:
    a. Hash all elements into a set // O(N) time, space
    b. Start with an element, check if is a starting members in set // O(1)
        b1. If no, early terminate and continue to next element in set
        b2. If yes, find out length of consecutive sequence 
    c. Keep track of largest sequence size


O(N) time complexity (every element processed once during sequence length determination)
O(N) space complexity (as we need to maintain a set of elements)
'''

def longest_consecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums_set = set(nums)
    result = 0

    # O(N) time complexity -> each element processed once
    for num in nums_set:
        # Skip if it not a starting element of some sequence
        if (num - 1) in nums_set:
            continue
        
        # Starting element of some sequence detected
        # Calculate length of consecutive sequence
        curr_seq_length = 1
        while (num + curr_seq_length) in nums_set:
            curr_seq_length += 1
        result = max(curr_seq_length, result)
    
    return result

    