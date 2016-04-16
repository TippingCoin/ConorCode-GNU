# ConorCode-GNU
The Conorcode libraries for python
# About:
Conorcode is a simple library for python, Protected By The GNU V3 Licence.
#Usage:
You are free to use ConorCode in any NOT-FOR-PROFIT project, if you plan on moneitizing it, move to a different library
There may be a ConorCode-Moneitization Project one day, to allow profit off my libraries, but not at the moment!

To Use This, you have to use the about() function from conorcode

Example

      import conorcode as code
      code.about()

#Modding
There is a file called mods.py, please use this as follows:

Example:

In Mods.py, type: 

      def MyFunction():

            print("Hello World")
      
Then in ConorCode.py, type:

      mods.MyFunction()

#Example file

SimpleAddCalculator.py:

      import conorcode as code
      code.about()
      code.add()
      
Whilst Conorcodes add function does this:

      import mods
      
      def add():
            print("Calculator V1 (Only Adds Numbers)")
            number1 = input("Enter First Number")
            number2 = input("Enter Second Number")
            print(number1+number2)
            print("Done")

#Modded Example File

Simple2FunctionCalculator.py:

      import conorcode as code
      code.about()
      code.mod-calc()
      
ConorCode.py:

      import mods
      
      def add():
            print("Calculator V1 (Only Adds Numbers)")
            number1 = input("Enter First Number")
            number2 = input("Enter Second Number")
            print(number1+number2)
            print("Done")
            
      'put mods below this line
      
      def mod-calc():
            func = input("Type - For Subtract and + for addition")
