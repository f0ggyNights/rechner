from Mathexpr import Mathexpr
from Arithmetic import calculate

from typing import List

class Token:
    def __init__(self, token, content):
        self.token = token
        # number            = 1
        # operator          = 2
        # paren left        = 3
        # paren right       = 4
        # not a valid token = 0

        self.content = content
        # operator: "+", "-" etc.
        # number: just the number
        # paren: 0 - content is not relevant for the parentesis

    def __str__(self):
        if self.token == 1: output = "number " + str(self.content)
        if self.token == 2: output = "operator " + self.content
        if self.token == 3: output = "paren_left"
        if self.token == 4: output = "paren_right"
        return ("["+output+"]")



# ////////////////////////////////////////////////////////
# //////////////////    tokenizer    /////////////////////
# ////////////////////////////////////////////////////////


def tokenize(txt: str) -> List[Token]:
    """Identifiziert die einzelnen Teile der eingegebenen Rechnung
    
    Der Input string wird in seine Bestandteile Zerlegt:
    Zahlen, Rechenoperatoren und Klammern.
    Jedes dieser Bestandteile wird durch ein Token Repräsentiert.
    Der Rückgabewert dieser Funktion ist die Liste der Token die in
    dem Eingabestring erkannt wurden."""

    def maybeDigit(txt):
        if txt == "":
            return False
        elif txt[0] in ["1","2","3","4","5","6","7","8","9","0"]:
            return True
        else:
            return False

    if txt == "":
        return []
    else:
        head, tail = txt[0], txt[1:]
        token = Token(0, 0)

        if head == "+": token = Token(2, "+")
        if head == "-": token = Token(2, "-")
        if head == "*": token = Token(2, "*")
        if head == "/": token = Token(2, "/")

        if head == "(": token = Token(3, 0)
        if head == ")": token = Token(4, 0)

        if maybeDigit(head):
            number = head
            while maybeDigit(tail):
                head, tail = tail[0], tail[1:]
                number += head
            token = Token(1, int(number))

        if token.token == 0:
            return tokenize(tail)
        else:
            return [token] + tokenize(tail)



# ////////////////////////////////////////////////////////
# //////////////////    parser    ////////////////////////
# ////////////////////////////////////////////////////////


# Takes an Operator and Returns its precedence.
# lower means gets calculatet first.
def operatorPrecedence(operator: Token) -> int:
    if operator.content in ["*", "/"]:
        return 0
    else:
        return 1


def parseRight(left: Mathexpr, tokens) -> Mathexpr:

    op, right, tail = tokens[0], tokens[1], tokens[2:]
    expr = Mathexpr(op.content, left, right.content)
    if len(tail) == 0:
        return expr
    else:
        return parseRight(expr, tail)  
    

# parses a math expression
def parseMath(tokens) -> Mathexpr:
    
    if len(tokens) == 1:
        return tokens[0].content
    else:

        # wen das erste Token eine öffnende Klammer ist Konsumieren wir diese
        # und machen beim nächsten Token weiter.
        if tokens[0].token == 3:
            return parseMath(tokens[1:])

        left, op, right, tail = tokens[0], tokens[1], tokens[2], tokens[3:]
        expr = Mathexpr(op.content, left.content, right.content)

        if len(tail) == 0:
            return expr
        else:
            # wenn das nächste Token eine Schließende Klammer ist
            # überspringen wir sie und ignorieren die Rangordnung des
            # nächsten Operators.
            if tail[0].token == 4:
                return parseRight(expr, tail[1:])
            
            # wenn das nächste Token ein Operator ist und dieser vorrang vor
            # dem aktuellen Operanden hat Parsen wir seine Operation und
            # nehmen diese als rechten Operanden dieser Operation.
            if tail[0].token == 2 and operatorPrecedence(op) > operatorPrecedence(tail[0]):
                return Mathexpr(op.content, left.content, parseMath(tokens[2:]))
            else:
                return parseRight(expr, tail)



def parse(txt: str) -> Mathexpr:

    # tokenizing the user input
    tokens: List[Token] = tokenize(txt)
    for token in tokens:
        print(token)

    # parsing the math expression
    expression = parseMath(tokens)
    print(expression)

    return expression


# ////////////////////////////////////////////////////////
# //////////////////    tests    /////////////////////////
# ////////////////////////////////////////////////////////

print(calculate(parse("(2+3)*4")))