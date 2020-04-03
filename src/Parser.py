class __token__:
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

    def Print_pretty(self):
        output = "token: "
        if self.token == 1: output += "number: " + str(self.content)
        if self.token == 2: output += "operator " + self.content
        if self.token == 3: output += "paren_left"
        if self.token == 4: output += "paren_right"
        print(output)


def parse(inputString):
    from Mathexpr import Mathexpr

    # returns a list of tokens
    def tokenize(txt):

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
            token = __token__(0, 0)

            if head == "+": token = __token__(2, "+")
            if head == "-": token = __token__(2, "-")
            if head == "*": token = __token__(2, "*")
            if head == "/": token = __token__(2, "/")

            if head == "(": token = __token__(3, 0)
            if head == ")": token = __token__(4, 0)

            if maybeDigit(head):
                number = head
                while maybeDigit(tail):
                    head, tail = tail[0], tail[1:]
                    number += head
                token = __token__(1, int(number))

            if token.token == 0:
                return tokenize(tail)
            else:
                return [token] + tokenize(tail)
            
    tokens = tokenize(inputString)
    for token in tokens:
        token.Print_pretty()

    return Mathexpr("+", 23, 545)
    # function not implemented yet - but returns a valid result for testing other modules.


# //////////////////////////////////////////////////////////////////////////
# //////////////////    tests    ///////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////
print("test")
parse("12*(3-34)")