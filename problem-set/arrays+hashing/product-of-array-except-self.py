'''
Problem Statement: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

'''
Initial Thoughts

1. What are the constraints?
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    No division allowed
    O(n) time complexity
    O(1) space complexity

2. Approach
    a. Observe that a product of array except self for an nums[i] 
        = product of all elements before nums[i] * product of all elements after nums[i]
    b. Create a result array of length = len(nums)

    For each num[i] in nums: // O(N) time
        c. Calculate Prefix Rolling Product (Start -> End)  and set it in result[i]

    For each num[i] in nums (in reverse order): // O(N) time
        d. Calculate Suffix Rolling Product (End -> Start) and multiply with result[i] (a.k.a prefix[i])
            to get actual answer

Overall O(N) time, O(1) space; N = len(nums)
'''

def product_except_self(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # O(1) Space -> Result array is not counted, based on question requirements
    suffix = 1
    result = [1] * len(nums)

    # Prefix Processing (From Beginning -> End) [O(N) time]
    for i in range(1, len(nums)):
        result[i] = result[i - 1] * nums[i - 1]

    # Suffix Processing (From End -> Beginning) [O(N) time]
    for j in range(len(nums) - 2, -1, -1):
        suffix *= nums[j + 1]
        result[j] *= suffix
            
    return result






