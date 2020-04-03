from Mathexpr import Mathexpr

import numbers

def calculate(expr):
    if expr is Mathexpr:
        left = expr.left if expr.left is not Mathexpr else calculate(expr.left)
        right = expr.right if expr.right is not Mathexpr else calculate(expr.right)
        op = expr.operator

        """
        #sieht hübscher aus, ist aber fehleranfällig zB right = 0
        operate = {
            "+" : left + right,
            "-" : left - right,
            "*" : left * right,
            "/" : left / right
        }
        return operate[op]
        """

        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "*":
            return left * right
        elif op == "/":
            return left / right

    elif isInstance(expr, numbers.Number):
        return expr

    else:
        import sys
        print("Not an Expression", file = sys.stderr)
