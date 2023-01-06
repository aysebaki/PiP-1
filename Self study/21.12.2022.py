"Tuples, Sets"

my_tuple1 = ("choco", "jelly", "chips")
print(my_tuple1)

#Tuple items are ordered, unchangeable, and allow duplicate values.
#first index is [0] and the second index is [1],... etc.
#the items in tuples have a defined order, and that order will not change.
#we cannot change, add or remove items after the tuple has been created.
#Since tuples are indexed, they can have items with the same value:

my_tuple2 = ("choco", "jelly", "chips", "choco", "jelly", "chips")
print(my_tuple2)

print(len(my_tuple2))

my_tuple3 = ("choco",)
print(type(my_tuple3))                     #for a one list item to be considered a tuple we have to add a comma

my_tuple_3 = ("choco")
print(type(my_tuple_3))                    #this won't be considered a tuple

my_tuple_a = ("apple", "banana", "cherry")
my_tuple_b = (1, 5, 7, 9, 3)                             #tuples can be of any data type
my_tuple_c = (True, False, False)
my_tuple_d = ("abc", 34, True, 40, "male")               #tuples can contain several datatypes at once

my_tuple4 = tuple(("choco", "jelly", "chips"))    #the code tuple(()) could also be used to create tuples
print(my_tuple4)
#####

my_tuple5 = ("choco", "jelly", "chips")
print(my_tuple5[1])

my_tuple6 = ("choco", "jelly", "chips")
print(my_tuple6[-1])

my_tuple7 = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
print(my_tuple7[2:6])

my_tuple8 = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
print(my_tuple8[:6])

my_tuple9 = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
print(my_tuple9[2:])

my_tuple10 = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
print(my_tuple10[-6:-2])

my_tuple11 = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
if "cookies" in my_tuple11:
    print("Yes, 'cookies' is in my_tuple11!")
else:
    print("No, 'cookies' is not in my_tuple11!")

#####

#once created, you cannot change a tuples value, BUT there is a way

a = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
b = list(a)
b[3] = "chip_cookies"          #we change the tuple to a list, change the value, and then turn it back to a tuple
a = tuple(b)
print(a)

c = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
d = list(c)
d.append("syrup")             #we change the tuple to a list, add a value, and then turn it back to a tuple
c = tuple(d)
print(c)

e = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
f = ("bar", "nutella")
e += f                       #we add tuple f to tuple e
print(e)

g = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
h = list(c)
h.remove("jelly")             #we change the tuple to a list, remove a value, and then turn it back to a tuple
g = tuple(h)
print(g)

i = ("choco", "jelly", "chips", "cookies", "cakes", "sweets", "biscuits")
del i

#####

my_tuple_fruits = ("apple", "pear", "orange", "strawberry")
(yellow, green, orange, red) = my_tuple_fruits               #this is called unpacking a tuple
print(yellow)                                                #the amount of values must match
print(green)
print(orange)
print(red)

my_tuple_fruits2 = ("apple", "pear", "orange", "strawberry", "rasberry", "cherry", "pomogranede")
(yellow, green, orange, *red) = my_tuple_fruits2             #if the amount of values don't match we use a *
print(yellow)
print(green)
print(orange)
print(red)

my_tuple_fruits3 = ("apple", "pear", "strawberry", "rasberry", "cherry", "pomogranede", "orange" )
(yellow, green, *red, orange) = my_tuple_fruits3             #if the amount of values don't match we use a *
print(yellow)
print(green)
print(red)
print(orange)

#####

my_tuple12 = ("tomatoes", "cucumber", "lettuce", "onion")
for x in my_tuple12:
    print(x)                                                    #loops in tuples

my_tuple13 = ("tomatoes", "cucumber", "lettuce", "onion")
for y in range(len(my_tuple13)):
    print(y)

my_tuple14 = ("tomatoes", "cucumber", "lettuce", "onion")
z = 0
while z < len(my_tuple14):
    print(my_tuple14[z])                                       #while loop in tuples
    z = z + 1

#####

tuple1 = ("tomatoes", "cucumber", "lettuce", "onion")
tuple2 = (1, 2, 3, 4)
tuple3 = tuple1 + tuple2                                       #adding tuples
print(tuple3)

tuple4 = ("tomatoes", "cucumber", "lettuce", "onion")
tuple5 = tuple4 * 2                                           #multiply tuple
print(tuple5)

"######################################################################################################################"

#Set items are unordered, unchangeable, and do not allow duplicate values.
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can remove items and add new items.
#Sets cannot have two items with the same value.

myset1 = {"apple", "banana", "cherry"}
print(myset1)

myset2 = {"apple", "banana", "cherry", "apple"}
print(myset2)                                      #no item two times with the same value

print(len(myset1))

set_a = {"apple", "banana", "cherry"}
set_b = {1, 5, 7, 9, 3}                            #sets can be of any data type
set_c = {True, False, False}
set_d = {"abc", 34, True, 40, "male"}              #a set with different data types

print(type(myset1))

myset3 = set(("apple", "banana", "cherry"))      #we can write sets with set(())
print(myset3)

#####

myset4 = {"apple", "banana", "cherry"}
for h in myset4:
    print(h)

myset5 = {"apple", "banana", "cherry"}
print("banana" in myset5)

#####

myset6 = {"apple", "banana", "cherry"}
myset6.add("pear")
print(myset6)

myset7 = {"apple", "banana", "cherry"}
myset8 = {"strawberry", "rasberry", "blueberry"}
                                                    #we are addind two sets together
myset7.update(myset8)
print(myset7)


myset9 = {"apple", "banana", "cherry"}
mylist9 = ["strawberry", "rasberry", "blueberry"]
                                                  #we are adding a set and a list together
myset9.update(mylist9)
print(myset9)

#####

myset10 = {"apple", "banana", "cherry"}
myset10.remove("apple")                           #removes one item
print(myset10)

myset11 = {"apple", "banana", "cherry"}
myset11.discard("banana")                         #removes one item
print(myset11)

myset12 = {"apple", "banana", "cherry"}
j = myset12.pop()
print(j)
print(myset12)

myset13 = {"apple", "banana", "cherry"}
myset13.clear()                                   #clears the whole set
print(myset13)

myset14 = {"apple", "banana", "cherry"}
del myset14                                       #deletes the whole set

#####

myset15 = {"apple", "banana", "cherry"}
for k in myset15:
    print(k)                                     #loop

#####

set16 = {"a", "b" , "c"}
set17 = {1, 2, 3}
set18 = set16.union(set17)                      #unites two sets
print(set18)

set19 = {"a", "b" , "c"}
set20 = {1, 2, 3}
set19.update(set20)                             #updates set 19
print(set19)

set21 = {"apple", "banana", "cherry"}
set22 = {"google", "microsoft", "apple"}
set21.intersection_update(set22)               #only prints items present in both sets
print(set21)

set23 = {"apple", "banana", "cherry"}
set24 = {"google", "microsoft", "apple"}
set25 = set23.intersection(set24)             #only prints items present in both sets
print(set25)

set26 = {"apple", "banana", "cherry"}
set27 = {"google", "microsoft", "apple"}
set26.symmetric_difference_update(set27)      #prints everything except duplicates
print(set26)

set28 = {"apple", "banana", "cherry"}
set29 = {"google", "microsoft", "apple"}
set30 = set28.symmetric_difference(set29)    #prints everything except duplicates
print(set30)
