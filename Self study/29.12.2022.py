"Dictionaries, If....ELse, While Loops, For Loops, Iterators"

my_dict1 = {"brand" : "apple",
            "model" : "promax",
            "color" : "silver",
            "year"  : 2022
            }
print(my_dict1)

#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

print(my_dict1["brand"])       #only prints the values of brand
print(len(my_dict1))
print(type(my_dict1))

my_dict2 = {                               #dict datatypes
  "brand": "Ford",                         #str
  "electric": False,                       #bool
  "year": 1964,                            #int
  "colors": ["red", "white", "blue"]       #list
}

my_dict3 = dict(name = "cutie", age = 23, country = "TR")             #using the dict function makes it into a dictionary
print(my_dict3)

#####

my_dict4 = {"brand" : "apple",
            "model" : "promax",
            "color" : "silver",
            "year"  : 2022
            }

a = my_dict4["year"]                              #you get the value of "year"
print(a)

b = my_dict4.get("year")                          #this method can also be used
print(b)

c = my_dict4.keys()                               #method will return a list of all the keys in the dictionary
print(c)


car1 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car1.keys()

print(x) #before the change

car1["color"] = "white"

print(x) #after the change


d = my_dict4.values()                              #method will return a list of all the values in the dictionary
print(d)

car2 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

y = car2.values()

print(y) #before the change

car2["color"] = "red"

print(y) #after the change

e = my_dict4.items()                               #method will return each item in a dictionary, as tuples in a list
print(e)

car3 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

z = car3.items()

print(z) #before the change

car3["year"] = 2020

print(z) #after the change

my_dict5 = {"brand" : "apple",
            "model" : "promax",
            "color" : "silver",
            "year"  : 2022
            }
if "year" in my_dict5:
    print("Yes, 'year' is one of the keys in the my_dict5 dictionary!")

#####

my_dict6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

my_dict6["year"] = 2018           #changes the values of "year"
print(my_dict6)

my_dict7 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

my_dict7.update({"year": 2020})  #updates the key "year"
print(my_dict7)

#####

my_dict8 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict8["color"] = "red"            #adds items
print(my_dict8)

my_dict9 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict9.update({"color": "red"})   #adds items with the update function
print(my_dict9)

#####


my_dict10 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict10.pop("model")                #removes item with the specified key name
print(my_dict10)

my_dict11 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict11.popitem()                  #removes the last inserted item
print(my_dict11)

my_dict12= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del my_dict12["model"]               #removes item with the specified key name
print(my_dict12)                     #the del function could also delete the entire dict

my_dict13 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict13.clear()
print(my_dict13)

#####

my_dict15 = {
    "color" : "grey",
    "length" : "35cm",
    "width" : "20cm",
    "type" : "cute"
}

for i in my_dict15:
    print(i)                            #prints all key names in the dict one by one

for j in my_dict15:
    print(my_dict15[j])                  #prints all values in the dict one by one

for k in my_dict15.values():
    print(k)                           #this method could also be used to print values

for l in my_dict15.keys():
  print(l)                             #returns the key of a dict

for m,n in my_dict15.items():
    print(m,n)                         #loop through both keys and values

#####

my_dict16 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict17 = my_dict16.copy()          #copies  dicts
print(my_dict17)

my_dict18 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict19 = dict(my_dict18)            #copies dicts
print(my_dict19)

#####

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#a dict that contains 3 dicts

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

"#########################################################################################################################################"

a = 20
b = 56
if a < b:
    print("a is smaller than b")

c = 33
d = 33
if c > d:
    print("c is greater than d")
elif c==d:
    print("c and d are equal")

e = 29
f = 57
if e > f:
    print("e is greater than f")
elif e == f:
    print("e and f are equal")
else:
    print("e is smaller than f")

g = 200
h = 33
if h > g:
  print("h is greater than g")
else:
  print("h is not greater than g")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 33
b = 200

if b > a:
  pass

"#########################################################################################################################################"

i = 1
while i < 6:                  #prints i as long as i is less than 6
    print(i)
    i+=1

i = 1
while i < 6:                 #exits loop when i is 3
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)                #continue if i is 3

i = 1
while i < 6:             #prints a message once the condition is false
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

"########################################################################################################################################"

fruits = ["apple", "banana", "cherry"]
for x in fruits:                           #prints each fruit in a fruit list
  print(x)

for x in "banana":                         #loop through a string
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:                           #exits the loop when x is banana
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:                          #break comes before print, banan gets left out completely
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:                          #does not print banana, continues with cherry
  if x == "banana":
    continue
  print(x)

for x in range(6):                        #goes from 0-5
  print(x)

for x in range(2, 6):
  print(x)                                #starts with two, does not include 6

for x in range(2, 30, 3):                 #jumps 3 steps
  print(x)

for x in range(6):                        #print all numbers from 0 to 5, and print a message when the loop has ended
  print(x)                                #else statement won't work if the loop gets stopped by a break
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:                           #combines every combo possible
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass

"##########################################################################################################################################"

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
                                                      #return an iterator from a tuple, and print each value
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
                                                     #also works with strings
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")
                                                   #iterate through a tuple
for x in mytuple:
  print(x)

mystr = "banana"
                                                  #iterate the characters of a string
for x in mystr:
  print(x)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
                                                #Create an iterator that returns numbers, starting with 1,
  def __next__(self):                           #and each sequence will increase by one (returning 1,2,3,4,5 etc.)
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
                                                 #stops after 20 iterations
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)