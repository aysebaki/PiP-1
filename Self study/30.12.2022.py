"Functions, Lambda, Arrays, Classes/Objects, Inheritance, Iterators "

#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

def my_function1():                        #defining a function
    print("Hello from a function")

def my_function1():
    print("Hello from a function")
my_function1()                              #calling a function

#in functions information is passed on via arguments
#arguments are written inside the parenthesis after a function is defined
#you can have multiple arguments as long as you seperate them with a comma
#the next example is gonna be fname, which basically is used to print the full name, it is better to understand visually

def my_function1(fname):
    print(fname + " Baki")                #the space before Baki is important, bc otherwise the names stick together

my_function1("Ayse")
my_function1("Kezban")
my_function1("Yavuz")
my_function1("Elif")
my_function1("öküz")

#a function must be called with the correct number of arguments
#ex. if you have two arguments you have to call the function with two arguments as well, not any more, not any less

def my_function2(fname, lname):
    print(fname + " " + lname)

my_function2("Ayse", "Baki")

#if the number of arguments is unknown we add a * before adding the parameter name(Arbitary Arguments, also called *args)

def my_function3(*kids):
    print("The eldest child is " + kids[0])

my_function3("Ayse", "Taha", "Elif")

#Keyword Arguments, also called kwargs
#the order of the aruments doesn't matter

def my_function4(child1, child2, child3):
    print("The youngest child is " + child3)

my_function4(child1 = "Ayse", child2 = "Taha", child3 = "Elif")

#if the number of keyword arguments is unknown we add ** before adding the parameter name

def my_function5(**kid):
    print("The kid's last name is " + kid["lname"])

my_function5(fname = "Elif", lname = "Baki")

#Default Parameter
#if we call a function without any arguments, it uses the default value

def my_function6(country = "Türkiye"):
    print("I am from " + country)

my_function6("Austria")
my_function6()

#Passing Lists as Arguments

def my_function7(food):                                 #I basically replace food with fruits, when I call the function with berries
    for x in food:
        print(x)

berries = ["raspberry", "strawberry", "blueberry"]

my_function7(berries)

def my_function8(y):                        #using the return value
    return 7 * y

print(my_function8(5))
print(my_function8(7))
print(my_function8(9))

#function definitions cannot be empty, but if we need it to be empty we can use the pass function to avoid errors

def my_function9():
    pass

#Recursion
#a function calls itsef. we can loop through the data and reach a result
#be very careful when writing it, sinnce it can go wrong easily

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results")
tri_recursion(6)

"#########################################################################################################################################"

x = lambda a : a + 7             #we add 7 to the argument a, and return the result
print(x(5))

y = lambda a,b : a * b
print(y(4,5))

z = lambda a,b,c : a + b - c
print(z(8,9,1))

#Why use lambda?
#lambdas are useful when you use them as anonymus functions inside other functions

def my_function10(n):
    return lambda a : a * n

my_doubler = my_function10(2)             #this definition always doubles the number we send in
print(my_doubler(11))

def my_function10(n):
    return lambda a : a * n

my_tripler = my_function10(3)             #this definition always triples the number we send in
print(my_tripler(11))

"#######################################################################################################################################"

cars = ["BMW", "Audi", "Mercedes"]

car1 = "BMW"
car2 = "Audi"                     #this is an array
car3 = "Mercedes"

x = cars[0]                       #this is how we acces elements of arrays
cars[0] = "BMW"

y = len(cars)                     #printing the length of arrays
print(y)

for x in cars:                    #looping an array
    print(x)

cars.append("VW")                 #adding elements to an array

cars.pop(1)                       #deletes the second element in the array

cars.remove("Mercedes")           #removes the element Mercedes from the array

"########################################################################################################################################"

class my_class1:
    x = 5

p1 = my_class1()
print(p1.x)

#__init()__ function
#Use the __init__() function to assign values to object properties,
#or other operations that are necessary to do when the object is being created

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person("Ayse", 20)

print(p2.name)
print(p2.age)

#__str__ function
#the __str__() function controls what should be returned when the class object is represented as a string

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p3 = Person("Ayse", 20)

print(p3)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("Hello my name is " + self.name)

p4 = Person("Ayse", 20)
p4.my_func()

#we can use other things instead of self
#here I used mine

class Person:
    def __init__(mine, name, age):
        mine.name = name
        mine.age = age

    def __str__(mine):
        return f"{mine.name}({mine.age})"

p5 = Person("Ayse", 20)

print(p5)

p5.age = 25         #set the age of p5 to 25
del p5.age          #delete the age of p5
del p5              #delete p5

class Person:
    pass

"####################################################################################################################################"

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

"#####################################################################################################################################"

#An iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#Technically, in Python, an iterator is an object which implements the iterator protocol,
#which consist of the methods __iter__() and __next__().

#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from

my_tuple1 = ("apple", "banana", "cherry")           #tuples
my_it = iter(my_tuple1)

print(next(my_it))
print(next(my_it))
print(next(my_it))

my_string1 = "banana"                             #strings can also be used
my_it = iter(my_string1)

print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))

my_tuple2 = ("apple", "banana", "cherry")
for x in my_tuple2:                               #loops in iterables
    print(x)

my_string2 = "apple"
for x in my_string2:
    print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
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

  def __next__(self):
    if self.a <= 20:                  #stops after 20 iterations
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

  