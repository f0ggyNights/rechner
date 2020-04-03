import src.Parser as Parser

if __name__ == "__main__":
    print("Type \"quit\" to stop program\n")
    txt = input()
    while(txt != "quit"):
        print(Parser.test(txt))
        txt = input()