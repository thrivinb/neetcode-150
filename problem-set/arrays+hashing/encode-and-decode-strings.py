''' 
Problem Statement: https://www.lintcode.com/problem/659/

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode
'''

'''
Initial Thoughts:

1. We definitely need to delimit the strings to help in the decoding process.
2. However, what if the delimiter appears inside the string? -> then we may end up doing extra tokenisation.
3. Instead, we should delimit the strings with a combination of:
    a. the number of characters of the word .
    b. some character (e.g. %) following it, so that we can handle case of > 1 digit of length
    
4. So the above will mean the delimiter looks something like 3%{word with 3 characters}40%{word with 40 characters}
5. Then, even if the original string does have 3%, we can always skip. Since we prefix original words, once we encounter our delimiter,
    we can merely jump by the number of characters required to reach the next delimiter, if any.
    This solves the problem of over-tokenisation.

Analysis:
O(N) time complexity, where N = number of words
Space complexity analysis not applicable, as no data structure is used to store anything in-memory.
'''

DELIMITER = "@"

"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    tokens = []
    for string in strs:
        tokens.append(str(len(string)) + DELIMITER)
        tokens.append(string)
    return "".join(tokens)

"""
@param: string: A string
@return: decodes a single string to a list of strings
"""
def decode(string):
    next_token_length = ""
    index_pointer = 0
    str_length = len(string)
    result = []

    while (index_pointer < str_length):
        char = string[index_pointer]
        if char != DELIMITER:
            next_token_length += char
            index_pointer += 1
            continue

        # DELIMITER spotted
        offset = int(next_token_length)
        result.append(string[index_pointer + 1: index_pointer + 1 + offset])
        index_pointer += offset + 1
        next_token_length = ""

    return result
    
# Test Cases
input_arr_1 = ["neet","code","lo@2ve","you"]
input_arr_2 = ["vineeth@@2", "@3says", "@10longwordhello"]
print(decode(encode(input_arr_1)) == input_arr_1)
print(decode(encode(input_arr_2)) == input_arr_2)

