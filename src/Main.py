import Parser as Parser
import Arithmetic as Arithmetic

if __name__ == "__main__":
    print("Type \"quit\" to stop program\n")
    txt = input()
    while(txt != "quit"):
        print(Parser.parse(txt))
        txt = input()