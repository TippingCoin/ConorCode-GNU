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

BaseApplication.py:

      import ConorCode as code
      code.about()
      #Don't touch the above, that protects my work, thanks :)
      code.modcalc()

      
ConorCode.py:

      import mods
      #Conorcode, the coding api for python
      #    Copyright (C) 2016  Conor Howland
      #
      #   This program is free software: you can redistribute it and/or modify
      #    it under the terms of the GNU General Public License as published by
      #    the Free Software Foundation, either version 3 of the License, or
      #    (at your option) any later version.
      #
      #    This program is distributed in the hope that it will be useful,
      #    but WITHOUT ANY WARRANTY; without even the implied warranty of
      #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
      #    GNU General Public License for more details.
      #
      #    You should have received a copy of the GNU General Public License
      #    along with this program.  If not, see <http://www.gnu.org/licenses/>.
      def about():
        print("ConorCode  Copyright (C) 2016  Conor Howland")
        print("This program comes with ABSOLUTELY NO WARRANTY.")
        print("This is free software, and you are welcome to redistribute it")
        print("under certain conditions; To View Licence, See Licence.txt or")
        print("http://www.gnu.org/licenses/")
        print(" ")
      def add():
        print("Calculator V1 (Only Adds Numbers)")
        number1 = input("Enter First Number")
        number2 = input("Enter Second Number")
        print(number1+number2)
        print("Done")

      #put mods below this line
      def modcalc():
        mods.modcalc()

Mods.py:

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

