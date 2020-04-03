from Mathexpr import Mathexpr

import numbers

def calculate(expr):
    if isinstance (expr, Mathexpr):
        left = expr.left if not isinstance (expr.left, Mathexpr) else calculate(expr.left)
        right = expr.right if not isinstance (expr.right, Mathexpr)else calculate(expr.right)
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

    elif isinstance(expr, numbers.Number):
        return expr

    else:
        import sys
        print("Not an Expression", file = sys.stderr)