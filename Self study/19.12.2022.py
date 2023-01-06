"Intro + Get started, Syntax, Comments, Variables, Data Types, Numbers, Casting, Strings"


print("Hello everyone!")

"###########################################################################################"

if 7 > 10:
    print("7 is greater than 10!")

x=29
y="my name is"

print(x)
print(y)

print(str(x))            #different types a variable can be written in
print(int(x))
print(float(x))

print(type(x))           #prints out if the variables type (e.g: str,float,int)
print(type(y))

"################################################################################################"
z = "incredible"

def myfunc():
    print("I feel " + z)

myfunc()


def myfunc():
    z = "awesome"                       # a variable created inside the function code will stay local.
    print("I feel " + z)                # the other variable created outside will stay global.

myfunc()

print("I feel " + z)

def myfunc():
    global z
    z = "fantastic"

myfunc()

print("I feel " + z)

"###############################################################################################"

a = 23
b = -6729
c = 45.7
d= 65e12
e = 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

###

r = float(a)
s = int(d)                         #used to convert variables from one type to another
t = complex(b)                     #complex numbers cannot be converted to another type

print(r)
print(s)
print(t)

print(type(r))
print(type(s))
print(type(t))

"##############################################################################################"

import random

print(random.randrange(1,1999))

"#############################################################################################"

l = """You can assign a multi line string to a variable by using three quotes.
I'm guessing that this would be of great help when printing a long text. 
It would also be good in the case of having to print something long more 
than once and still wanting some structer."""

print(l)          #the line breaks are in the same postion as in the code

m = "Hello my name is.....slim shady"
print(m[9])                               #0 is the first character

for n in "chromosome":
    print(n)

print(len(l))

txt = "This is really great! I really like the way things are going. My tempo could be better tho"
print("tempo" in txt)

txt = "This is really great! I really like the way things are going. My tempo could be better tho"
if "tempo" in txt:
    print("Yes, 'tempo' is present.")

txt = "This is really great! I really like the way things are going. My tempo could be better tho"
print("intrusive" not in txt)

txt = "This is really great! I really like the way things are going. My tempo could be better tho"
if "intrusive" not in txt:
    print("No, 'intrusive' is not present.")

###
p = "Whats up everyone? I'm a clone and I'm here to destroy the world HAHAHAHAHAHAH"
print(p[3:7])                  #gets the characters from 3-7. 7 is not included

print(p[:7])                   #starts from the beginning

print(p[1:])                   #goes until the end

print(p[-7:-3])                #starts from negatives. 3 is not included

#####
print(p.upper())               #returns string in uppercase
print(p.lower())               #returns string in lowercase
print(p.strip())               #removes whitespace
print(p.replace("H","J"))      #replaces h's with j's
print(p.split("?"))            #turns string into subset by dividing it with ?

q = l + p                      #combines two strings
print(q)

q = l + " " + p               #combines two strings but adds a space in-between
print(q)

age = 20
w = "Hello I am Ayse and I am {}."
print(w.format(age))          #we use format to combine numbers and strings

amount = 10
size = 20
shipment_length = 3
v = "Hello I would like to get {} boats that are at least {} meters in legth. And I want them delivered under {} days.  "
print(v.format(amount, size, shipment_length))      #we can use format for unlimited amounts of arguments

######

u = "We are the so called \"Kanacken\" of Austria."
print(u)

#####