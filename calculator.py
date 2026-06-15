""" this  calculator  can perform basic arithmetic operations plus warning some errors like dividing with zero and invalid input"""


def math():
    print(f"\nhello! let's do some maths today.\n")
    def calculas():
        try:
            num1 = float(input("enter the first number: "))
            num2 = float(input("enter the second number: "))
            
            sign = input(f"choose a sign btn +,-,*,/ \n")

            if sign not in ("+", "-", "*", "/"): # finally i hope there is no any room for errors after i solved this one!!
                 print(f"\nthat's not a standard sign.\nplease next time choose btn +,-,* or /\nlet's start over.")
                 return calculas()
            
            print(f"then the answer is:")
            if sign == "+":
                    print(num1 + num2) # we only print not return
            elif sign == "-":
                print(num1 - num2)
            elif sign == "*":
                print(num1 * num2)
            elif sign == "/":
                    if num2 == 0:
                        print("division error! you can't divide with zero.")
                    else:
                        print(num1 / num2)
            def playagain():#this is avoiding the not in y and n break
                again = input(f"\nwant to keep on calculating? \nenter:y for yes or n for no\n")
                if again == "y":
                    print("\nokay! let's go again")
                    return calculas()
                elif again == "n":
                    print("thx to calculate with us! bye bye👋👋👋")
                else:
                    print("hey! you must choose btn y & n")
                    return playagain()
            playagain()
                
        except ValueError:
            print(f"please type in only numbers.\n")
            return calculas()
            
    calculas()

math()