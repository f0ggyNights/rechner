import Parser as Parser
import Arithmetic as Arithmetic

if __name__ == "__main__":
    print("Type \"quit\" to stop program\n")
    txt = input()
    while(txt != "quit"):
        expression = Parser.parse(txt)
        result = Arithmetic.calculate(expression)
        print(result)
        txt = input()