''' 
Problem Statement: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

'''
Initial Thoughts:

1. What are the constraints?
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters. 

# Since input set is only consisting LOWERCASE English letters -> at maximum, there are 26 different characters to analyse.
# Memory O(1)
# Time O(N), where N = Max(length(s), length(t))

'''

def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    # Since input is only lower-case English characters, create a size 26 array to count frequency
    char_freq_array = [0] * 26 

    # populate char frequency array of string s
    for char in s:
        index = ord(char) - ord('a')
        curr_count = char_freq_array[index]
        char_freq_array[index] = curr_count + 1
    
    # decrement char frequency array of string t
    for char in t:
        index = ord(char) - ord('a')
        curr_count = char_freq_array[index]
        if curr_count <= 0:
            return False
        char_freq_array[index] = curr_count - 1
    
    # if all frequencies were decremented to 0, means they are valid anagrams
    return all([v == 0 for v in char_freq_array])
  
            


  
            

