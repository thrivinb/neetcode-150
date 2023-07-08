'''
Problem Statement: https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. 

If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

'''
Initial Thoughts:
    Constraints:
        * 1 <= temperatures.length <= 10^5
        * 30 <= temperatures[i] <= 100

    Observations:
        Monotonic Descending Stack would solve this problem
        
        temperatures = [73,74,75,71,69,72,76,73]
        73: 0 -> [] 
        74: 1 -> [{73: 0}] -> since 74 > 73, pop from stack and set result[0] as 1 - 0 = 1
        75: 2 -> [{74: 1}] -> since 75 > 74, pop from stack and set result[1] as 2 - 1 = 1
        71: 3 -> [{75: 2}] -> since 71 < 75, do not pop from stack
        69: 4 -> [{71: 3}, {75: 2}] -> since 69 < 71, do not pop from stack
        72: 5 -> [{69: 4}, {71: 3}, {75: 2}] 
            -> since 72 > 69, pop and set result[4] as 5 - 4 = 1
            -> since 72 > 71, pop and set result[3] as 5 - 3 = 2
        76: 6 -> [{72: 5},{75:2}]
            -> since 76 > 72, pop and set result[5] as 6 - 5 = 1
            -> since 76 > 75, pop and set result[2] as 6 - 2 = 4
        73: 7 -> [{76:6}] since 73 < 76 do not pop from stack

        end: [{73:7}, {76:6}] do nothing (result[6] and result[7] is 0 by default)    
    
    Approach:
        1. Maintain monotonic decreasing stack
        2. Initialise result array of length n with 0
        3. For each temperature t and index i:
            a. while stack is non-empty and current t > top of stack's t
                a1. pop stack and find out index j of the popped temperature
                a2. set result[j] = i - j
            b. push (t, i) to stack
        4. return result
'''




def daily_temperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """

    # Maintain monotonic decreasing stack
    stack = []
    result = [0] * len(temperatures)

    for i, t in enumerate(temperatures):  
        # Pop all elements in stack that are lower than / equal to current temperature
        # Why? 
        # Since they wont be required for comparison with earlier days, 
        # as current day itself is greater than those evicted
        
        while stack and t > stack[-1][0]:
            stack_temp, stack_index = stack.pop()
            result[stack_index] = i - stack_index
    
        stack.append((t, i))
    
    return result
            