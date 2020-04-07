import Parser as Parser
import Arithmetic as Arithmetic



if __name__ == "__main__":

    print("Type \"quit\" to stop program\nType \"details 0/1\" to stop show or not show parser details.\n")
    showdetails = False

    txt = input(">> ")

    while(txt != "quit"):
        if txt.startswith("details"):
           if txt.split()[1] == "1": showdetails = True
           if txt.split()[1] == "0": showdetails = False 
        else:
            expression = Parser.parse(txt)
            result = Arithmetic.calculate(expression)
            if showdetails:
                tokens = Parser.tokenize(txt)
                tokenstring = "tokens: "
                for t in tokens:
                    tokenstring += str(t)
                print(tokenstring)
                print("Parser:", expression)
                print("Arithmetic:", result)
            else:
                print(result)

        txt = input(">> ")