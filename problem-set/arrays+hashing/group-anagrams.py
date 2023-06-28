'''
Problem Statement: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.
'''

'''
Initial Thoughts

1. What are the constraints?
    1 <= strs.length <= 10^4 (Total number of strings)
    0 <= strs[i].length <= 100 (Each string is at most 100 characters, and can also be empty)
    strs[i] consists of lowercase English letters.

2. We can encode these strings into a constant size string representation and hash them based on string representation

N = num strings
Encoding: O(N) time (N O(1) operations)
Grouping by encoding: O(N) space, O(N) time
'''

def encode_str(str_input):
    base_arr = [0] * 26
    for char in str_input:
        index = ord(char) - ord('a')
        curr_count = base_arr[index]
        base_arr[index] = curr_count + 1
    numbers_as_str = [str(num) for num in base_arr]
    return ','.join(numbers_as_str)

def group_anagrams(strs):
    result = dict()
    for str in strs:
        output = encode_str(str)
        if output not in result:
            result[output] = [str]
        else:
            result[output].append(str)
    
    return result.values()

