'''
Problem Statement: https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

'''
Initial Thoughts

1. What are the constraints?
    1 <= n <= 8

2. Approach:
    - Understand that this is a combinatorics kind of question
    - Brute Force approach would be to generate all permutations and run the valid parentheses check on each generated string
    - But can we do clever generations to ensure validity in the first place?
        a. A close bracket can only come after an open bracket
        b. In total, there should be n open brackets, and n close brackets
    - With the above 2 rules, we can define a backtracking function
        a. Maintain a stack containing the parentheses characters (for efficient concatenation using join)
        b. BASE CASE: When we have n open and n close brackets, join the stack, append this to result list and return
        c. Call #1: If num_open < n, we can continue to add an open bracket 
            c1. Push '(' to stack
            c2. Recurse with num_open + 1
            c3. Pop stack once above call has returned
        d. Call #2: If num_close < n and num_close < num_open, we can safely add a close bracket
            d1. Push ')' to stack
            d2. Recurse with num_close + 1
            d3. Pop stack once above call has returned
        e. Return result

3. Asymptotic Analysis:
    - Temp Stack:
        - O(n) space -> at most 2n characters in a stack at any single timeframe 
    - Result List:
        - O(C(n)) space, where C(n) is the Catalan number, which is approximately 4^n / n^(3/2)
    - Time Complexity:
        - O(C(n)) space, where C(n) is the Catalan number, which is approximately 4^n / n^(3/2)
'''    

def generate_parentheses(n):
    """
    :type n: int
    :rtype: List[str]
    """

    result = []
    # Keeps track of string characters so far
    stack = []

    def backtrack(num_open, num_close):
        if num_open == n and num_close == n:
            # reached base case
            result.append("".join(stack))
            return
            
        if num_open < n:
            stack.append("(")
            backtrack(num_open + 1, num_close)
            stack.pop()
        
        if num_close < n and num_close < num_open:
            stack.append(")")
            backtrack(num_open, num_close + 1)
            stack.pop()

    backtrack(0, 0)
    return result