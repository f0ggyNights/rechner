import sys

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
OPERATORS = ["+", "-", "*", "/"]
PARENTHESIS = ["(", ")"]
IGNORE = [" "]
VALID_CHARACTERS = DIGITS + OPERATORS + PARENTHESIS


# checks if a mathematical expression represented as a String is valid
def validate(stringexpr) -> bool:
    if stringexpr.count(PARENTHESIS[0]) != stringexpr.count(PARENTHESIS[1]):
        return False

    expr = []

    # ignore spaces except for spacing between digits, in that case return false
    for i in range(len(stringexpr)):
        s = stringexpr[i]
        # check for spaces between digits
        if len(expr) > 0 and s in DIGITS and expr[-1] in DIGITS and stringexpr[i-1] in IGNORE:
            print("illegal syntax:\n{}\n{}^".format(stringexpr, " "*(i-1)), file=sys.stderr)
            return False
        # check for valid characters
        if s in VALID_CHARACTERS:
            expr.append(s)
        elif s not in IGNORE:
            print("illegal character: {}\n{}\n{}^".format(s, stringexpr, " "*i, file = sys.stderr))
            return False

        

    

    for i in range(len(expr)):
        
        # if expr[i] is an operator or open parenthesis and it's the last character 
        # or following character isn't a digit or open parenthesis
        if expr[i] in OPERATORS + [PARENTHESIS[0]] and (len(expr) == i+1 or expr[i+1] not in DIGITS + [PARENTHESIS[0]]) or i == 0 and expr[i] in OPERATORS:   
            return False

    return True

print(validate(" (3) "))