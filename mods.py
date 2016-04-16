import ConorCode as code
def modcalc():
    func = raw_input("Type - For Subtract and + for addition")
    if func in ["+","add","Add","ADD"]:
            code.add()
    elif func in ["-","minus","subtract","Subtract","SUBTRACT"]:
            subtract()

def subtract():
        print("Calculator V1 (Only Subtract Numbers)")
        number1 = input("Enter First Number")
        number2 = input("Enter Second Number")
        print(number1-number2)
        print("Done")
