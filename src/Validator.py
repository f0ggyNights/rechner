import sys

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
OPERATORS = ["+", "-", "*", "/"]
PARENTHESES = ["(", ")"]
IGNORE = [" "]
VALID_CHARACTERS = DIGITS + OPERATORS + PARENTHESES


# checks if a mathematical expression represented as a string is valid
def validate(stringexpr) -> bool:
    expr = []
    error = ValidationError("", "", -1)
    openparens = 0

    # check if parentheses are closed properly
    if stringexpr.count(PARENTHESES[0]) > stringexpr.count(PARENTHESES[1]):
        error = ValidationError(stringexpr, "parenthesis not closed:", stringexpr.rfind(PARENTHESES[0]))
    
    # ignore spaces except for spacing between digits, in that case return false
    for i in range(len(stringexpr)):
        s = stringexpr[i]

        # check for valid characters
        if s in VALID_CHARACTERS:
            expr.append(s)
        elif s not in IGNORE:
            error = ValidationError(stringexpr, "illegal character", i)
            break

        # check if parens are open
        if s in PARENTHESES:
            if s == PARENTHESES[0]:
                openparens += 1
            if s == PARENTHESES[1]:
                if openparens == 0:
                    error = ValidationError(stringexpr, "no matching parenthesis", i)
                    break
                openparens -= 1

        if len(expr) > 1:
            # check if operator is followed by operator or closed parenthesis  
            if expr[-2] in OPERATORS and s in OPERATORS + [PARENTHESES[1]]:

                if not (s == OPERATORS[1] and expr[-2] != OPERATORS[1]):
                    error = ValidationError(stringexpr, "consecutive operator", i)
                    break
            
            # missing operator
            if s == PARENTHESES[0] and expr[-2] in DIGITS:
                error = ValidationError(stringexpr, "missing operator", i-1)
                break

            # check for spaces between digits
            if s in DIGITS and expr[-2] in DIGITS and stringexpr[i-1] in IGNORE:
                error = ValidationError(stringexpr, "missing operator", i-1)
                break    

    
    
    # if no other error occured and last valid char is operator or open parenthesis
    if error.pos == -1 and expr[-1] in OPERATORS + [PARENTHESES[0]]:
        error = ValidationError(stringexpr, "invalid syntax", stringexpr.rfind(expr[-1]))

    #actual error
    if error.pos != -1:
        print(error, file=sys.stderr)
        return False

    return True

class ValidationError:

    def __init__(self, expr, msg, pos):
        self.expr = expr
        self.msg = msg
        self.pos = pos

    def __str__(self):
        return "ValidationError:\n\t{}\n\t{}^\n\t{}\n".format(self.expr, " "*self.pos, self.msg)

#print(validate("1 + + (--1)"))