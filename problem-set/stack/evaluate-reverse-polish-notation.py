'''
Problem Statement: https://leetcode.com/problems/evaluate-reverse-polish-notation/

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation (Postfix Notation).

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    * The valid operators are '+', '-', '*', and '/'.
    * Each operand may be an integer or another expression.
    * The division between two integers always truncates toward zero.
    * There will not be any division by zero.
    * The input represents a valid arithmetic expression in a reverse polish notation.
    * The answer and all the intermediate calculations can be represented in a 32-bit integer.
'''

'''
Initial Thoughts:
    1. Division can be tricky (Non Integer Quotients truncate towards 0)
        - Negative quotients need to take math.ceil
        - Positive quotients need to take math.floor
    2. Operands can be inserted into stack
    3. When operator is encountered, pop top 2 operands and perform operation
'''

def is_integer(s):
    return s.isnumeric() or (s.startswith('-') and s[1:].isnumeric())

def eval_rpn(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for token in tokens:
            # Push to stack if operand
            if is_integer(token):
                stack.append(int(token))
                continue

            # Perform operation
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                is_quotient_negative = (operand1 < 0 or operand2 < 0) and (operand1 >= 0 or operand2 > 0)

                division_result = abs(operand1) // abs(operand2)
                if is_quotient_negative:
                    division_result *= -1

                stack.append(division_result)
            else:
                print("Invalid operator / structure of input")
            
        # return top of stack
        return stack[len(stack) - 1]


            