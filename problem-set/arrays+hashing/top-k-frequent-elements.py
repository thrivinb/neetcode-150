'''
Problem Statement: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

'''
Initial Thoughts

1. What are the constraints?
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

2. My approach:
    a. Create a frequency map of all elements in nums -> O(N) time, O(N) space [key: element, value: frequency]
    b. Sort the frequency map's entry set by value in descending order -> O(N log N) time, O(N) space 
    c. Iterate for first k keys in sorted map and append to result list -> O(k) time, O(k) space

    Overall -> O(N log N) time, O(N) space
'''

def top_k_frequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = dict()

        # Create Frequency Map O(N) time, O(N) space complexity (N = size of nums)
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] = freq_map[num] + 1
        
        # Sort by value O(N log N) time (N = number of key-value pairs)
        sorted_by_value = sorted(freq_map.items(), key=lambda x:x[1], reverse=True)

        result = []
        # Poll k-th highest key-value pair
        for x, y in sorted_by_value:
            if (k <= 0):
                break

            result.append(x)
            k -= 1
                
        return result
