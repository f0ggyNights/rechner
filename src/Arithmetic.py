from Mathexpr import Mathexpr
import numbers
import sys

def calculate(expr):
    if isinstance (expr, Mathexpr):
        # calculates left and right parts of the expression recursively
        left = expr.left if not isinstance (expr.left, Mathexpr) else calculate(expr.left)
        right = expr.right if not isinstance (expr.right, Mathexpr)else calculate(expr.right)
        op = expr.operator

    # "switch-case" for the base operators
    # calculates and returns result
    # prints error message if operator is not supported
        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "*":
            return left * right
        elif op == "/":
            return left / right
        else:
            print("Not an Operator: {}".format(op), file = sys.stderr)

    # expression is a number, so just return it
    elif isinstance(expr, numbers.Number):
        return expr

    # Not a supported expression
    else:
        print("Not a valid expression", file = sys.stderr)