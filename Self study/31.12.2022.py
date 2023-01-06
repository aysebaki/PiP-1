"Scope,Modules, Dates, Math, RegEx, PiP, Try...Except, User Input, String Formatting"

#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function

def my_func1():
    x = 450
    print(x)
my_func1()

#As explained in the example above, the variable x is not available outside the function,
#but it is available for any function inside the function

def my_func2():
    x = 350
    def my_innerfunc2():
        print(x)
    my_innerfunc2()
my_func2()

#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.

y = 250

def my_func3():
    print(y)
my_func3()
print(y)

#If you operate with the same variable name inside and outside of a function,
#Python will treat them as two separate variables,
#one available in the global scope (outside the function)
#and one available in the local scope (inside the function)

x = 650

def my_func4():
    x = 250
    print(x)
my_func4()
print(x)

#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#The global keyword makes the variable global.

def my_func5():
    global z
    z = 750
my_func5()
print(z)

#Also, use the global keyword if you want to make a change to a global variable inside a function.

z = 550

def my_func5():
    global z
    z = 750
my_func5()
print(z)

"####################################################################################################################################"

#Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application.
#To create a module just save the code you want in a file with the file extension .py

import mymodule
                                #importing code from anpther file
mymodule.greeting("John")

import mymodule
                                   #again importing code from another file
a = mymodule.person1["age"]
print(a)

import mymodule as mx
                                  #creating an alias for mymodule with as
a = mx.person1["age"]
print(a)

import platform

x = platform.system()                        #built-in funtion
print(x)

import platform
                                            #built-in function
x = dir(platform)
print(x)

from mymodule import person1
                                            #we only imported the person1
print (person1["age"])

"#######################################################################################################################################"

#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime
                                           #import the datetime module and display the current date
x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()
                                         #returns the year and the weekday
print(x.year)
print(x.strftime("%A"))

import datetime

x = datetime.datetime(2020, 5, 17)
                                        #used to create a date
print(x)

import datetime

x = datetime.datetime(2018, 6, 1)
                                       #displays the name of the month
print(x.strftime("%B"))

"#######################################################################################################################################"

#Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers

x = min(5, 10, 25)
y = max(5, 10, 25)
                                    #min and max are to find the lowest and highest numbers
print(x)
print(y)

x = abs(-7.25)
                                    #returns the absolute value(positive value) for the sprecified number
print(x)

x = pow(4, 3)
                                    #basically returns vier hoch 3
print(x)

import math

x = math.sqrt(64)
                                    #square root of 64
print(x)

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)                           #rounds a number upwards to its nearest integer
print(y)                           #rounds a number downwards to its nearest integer, and returns the result

import math

x = math.pi                        #returns the value of pi

print(x)


"#################################################################################################################################"

#JSON is a syntax for storing and exchanging data.
#JSON is text, written with JavaScript object notation.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

"##########################################################################################################################################"

#a RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#regEx can be used to check if a string contains the specified search pattern.

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)                     #Search the string to see if it starts with "The" and ends with "Spain"

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)                    #prints a list of all matches
print(x)

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)              #returns an empty list if nothing was found
print(x)

#The search() function searches the string for a match, and returns a Match object if there is a match.
#If there is more than one match, only the first occurrence of the match will be returned

import re

txt = "The rain in Spain"
x = re.search("\s", txt)                             #Search for the first white-space character in the string

print("The first white-space character is located in position:", x.start())

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)                      #if no matches are found, the value None is reutned
print(x)

#The split() function returns a list where the string has been split at each match:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)                                    #Split at each white-space character
print(x)

#You can control the number of occurrences by specifying the maxsplit parameter

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)                                  #Split the string only at the first occurrence

print(x)

#The sub() function replaces the matches with the text of your choice:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)         #Replace every white-space character with the number 9
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)        #replace the first 2 occurasens
print(x)

#A Match Object is an object containing information about the search and the result

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

"############################################################################################################################################"

#PIP is a package manager for Python packages, or modules if you like
#A package contains all the files you need for a module.
#Modules are Python code libraries you can include in your project.

"###########################################################################################################################################"

#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
  print(c)                               #The try block will generate an exception, because x is not defined
except:
  print("An exception occurred")

try:
  print(x)
except NameError:                        # if the try block raises a NameError and another for other errors
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#You can use the else keyword to define a block of code to be executed if no errors were raised

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

x = -1
                                                   #Raise an error and stop the program if x is lower than 0
if x < 0:
  raise Exception("Sorry, no numbers below zero")

#The raise keyword is used to raise an exception.
#You can define what kind of error to raise, and the text to print to the user.

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

"#################################################################################################################################"

#Python allows for user input.
#That means we are able to ask the user for input.
#The method is a bit different in Python 3.6 than Python 2.7.
#Python 3.6 uses the input() method.

username = input("Enter username:")
print("Username is: " + username)

"##########################################################################################################################################"

#To make sure a string will display as expected, we can format the result with the format() method.
#The format() method allows you to format selected parts of a string.
#Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
#To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

price = 49
txt = "The price is {} dollars"                  #a placeholder for the price
print(txt.format(price))

txt = "The price is {:.2f} dollars"              #Format the price to be displayed as a number with two decimals

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Also, if you want to refer to the same value more than once, use the index number

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#You can also use named indexes by entering a name inside the curly brackets {carname},
#but then you must use names when you pass the parameter values txt.format(carname = "Ford")

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))