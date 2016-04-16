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
