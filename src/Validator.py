DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
OPERATORS = ["+", "-", "*", "/"]
PARENTHESIS = ["(", ")"]
VALID_CHARACTERS = DIGITS + OPERATORS + PARENTHESIS
IGNORE = [" "]



def isValid(stringexpr):
    if stringexpr.count(PARENTHESIS[0]) != stringexpr.count(PARENTHESIS[1]):
        return False
    
    expr = [c for c in stringexpr if c not in IGNORE]

    print(expr)
    """
    for i in range(len(expr)):
        if stringexpr in IGNORE:
            continue
        if stringexpr[i] not in VALID_CHARACTERS:
            return False
        if stringexpr[i] in OPERATORS and len(stringexpr) :
    """        
    
    return True

isValid("1 + 2")