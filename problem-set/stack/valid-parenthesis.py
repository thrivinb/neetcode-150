'''
Problem Statement: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

'''
Initial Thoughts

1. What are the constraints?
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'

2. Approach:
    a. Maintain a stack that is in charge of keeping all the open parenthesis
    b. For each character:
        b1. If opening parenthesis, push to stack
        b2. Else If stack non-empty and character is the matching closing parenthesis:
            pop stack
        b3. Else return False (wrong or early closing parenthesis encountered)
        
    c. Finally, return len(stack) == 0

    N = length of string s

    O(N) time -> N characters processed, with each step taking O(1) time to lookup matching parenthesis
    O(1) space -> O(N) In worst case, if input string consists of all opening characters
'''
def is_valid_parenthesis(s):
    """
    :type s: str
    :rtype: bool
    """

    stack = []
    matching_parenthesis = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        # Check if opening parenthesis
        if char in matching_parenthesis:
            stack.append(char)
        elif len(stack) > 0 and char == matching_parenthesis[stack[len(stack) - 1]]:
            # Pop if correct closing parenthesis
            stack.pop()
        else:
            return False

    return len(stack) == 0