'''
Problem Statement: https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
'''

'''
Constraints:
    * -2^31 <= val <= 2^31 - 1
    * Methods pop, top and getMin operations will always be called on non-empty stacks.
    * At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

Initial Thoughts:
    a. Stack already has O(1) push, pop and top operations
    b. Our job is to also add O(1) getMin 
    c. Key observation:
        - If elements pushed in decreasing order e.g. [3,2,1], currMin keeps decreasing
        - Once 1 gets popped, we need to update currMin
        - If after popping, stack gets empty, currMin should be reset to max value 
        - Do note that at the time an element is pushed, 
            whatever minimum there was at that time, it will continue to hold once the said element is again at top of stack
'''
class MinStack(object):
    # O(1) time
    def __init__(self):
        self.stack = []
        self.curr_min = 2 ** 31

    # O(1) time
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.curr_min = min(self.curr_min, val)
        self.stack.append((val, self.curr_min))
    
    # O(1) time
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if len(self.stack) != 0:
            curr_top = self.stack[len(self.stack) - 1]
            self.curr_min = curr_top[1]
        else:
            # Stack is empty, default to max value as curr_min
            self.curr_min = 2 ** 31

    # O(1) time
    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1][0]
        
    # O(1) time
    def getMin(self):
        """
        :rtype: int
        """
        return self.curr_min
        
