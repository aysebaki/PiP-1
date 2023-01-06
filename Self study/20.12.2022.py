"Booleans, Operators, Lists"


a = 29
b = 57

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")             #checking truth value?


print(bool("Whatsup"))
print(bool(4240))                           #evaluates a value and gives True or False in reteurn.


print(bool(34))                                          #every bool value returns True when the number is not 0
print(bool("heyyyy"))                                    #when the string is not empyt
print(bool(["red" , "orange" , "yellow"]))               #and when the list is  not empty

print(bool(0))                                           #bool returns False, when the number is 0
print(bool(""))                                          #when the string is empty
print(bool([]))                                          #when the list is empty
print(bool(()))                                          #when the tuple is empty.....
print(bool({}))
print(bool(False))                                       #when the value is False
print(bool(None))                                        #or None

#####

class my_class():
    def __len__(self):
        return 0
                                                        #returns False, when an object made with a class
my_obj = my_class()                                     #from a  __len__ function returns 0 or False
print(bool(my_obj))

###

def my_function():
    return True
                                                       #we can create functions that return boolean values
print(bool(my_function()))

###

def myfunction():
    return True
                                                      #we can execute codes based on boolean values of functions
if myfunction():
    print("YES!")
else:
    print("NO!")

###

c = 37
                                                      #isinstance checks whether an object is a certain data type or not
print(isinstance(c, int))

"#######################################################################################################################################"

my_list = ["cold" , "winter" , "wind" , "snow"]
print(my_list)                                       #the first item has the index [0]

my_list1 = ["cold" , "winter" , "wind" , "snow", "winter" , "cold"]
print(my_list1)                                      #there can be duplicates in a list

my_list2 = ["summer" , "sun" , "hot" , "breeze"]
print(len(my_list2))                                 #prints the length

my_list_a = ["these" , "are" , "words"]              #lists can be strings
my_list_b = [1, 2, 3, 4, 5]                          #integars
my_list_c = [True, False, True, True ]               #and booleans
print(my_list_a, my_list_b, my_list_c)

my_list_d = ["these" , 5 , True , "are" , False, 3 , "mixed"]              #lists can contain int,str and bool at the same time
print(my_list_d)

print(type(my_list))

my_list_e = list((["cold" , "winter" , "days"]))       #using list(()) is also a possibility
print(my_list_e)

###

my_list_f = ["i" , "am" , "freezing"]               #[0]is the first word. -1 is the last & -2 is the one before last
print(my_list_f[1])

print(my_list_f[-1])

my_list_g = ["hello", "everyone", "i", "would", "just", "like", "to", "let", "everyone", "know", "that", "i", "am", "cold"]
print(my_list_g[3:7])                              #index 3 is included, but 7 is not included
print(my_list_g[:7])                               #from beginning to 7, but does not include 7
print(my_list_g[3:])                               #from 3 until the very end
print(my_list_g[-8:-1])

if "like" in my_list_g:
    print("Yes, 'like' is in this list!")
else:
    print("No, 'like' is not in this list")

###

my_list_h = ["ama" ,  "ben" , "artik" , "bikmisam"]
my_list_h[3] = "bitmisem"                                       #replaces [3] with bitmisem
print(my_list_h)

my_list_i = ["cok" , "gereksiz" , "bos" , "islerle" , "ugrasiyoruz" , "bee"]
my_list_i[1:3] = ["sacma"]                                      #replaces [gereksiz][bos] with sacma
print(my_list_i)

my_list_j = ["cok" , "sacma" , "islerle" , "ugrasiyoruz" , "bee"]
my_list_j[1:2] = ["bos", "gereksiz"]                           #replaces [sacma] with bos gereksiz
print(my_list_j)

my_list_k = ["ben", "bu", "listlerde", "yoruldum", "artik"]
my_list_k.insert(2, "boklu")
print(my_list_k)                                               #adds object to a specific place in list

my_list_l = ["ama", "asko", "artik"]
my_list_l.append("yeto")                                       #adds object at the end of the list
print(my_list_l)

my_list_l.extend(my_list_k)                                    #adds list to another list
print(my_list_l)

my_tuple_1 = ("i", "am", "sick", "and", "tired")
my_list_j.extend(my_tuple_1)                                   #adds tuple to a list
print(my_list_j)

###

my_list_m = ["tukoh", "taka", "tukoh", "taka", "yalla", "habibti"]
my_list_m.remove("yalla")
print(my_list_m)

my_list_n = ["i", "am" , "gonna", "swiiiiiing", "from" , "the", "chandalier"]
my_list_n.pop(1)
print(my_list_n)                                              #removes one specific index,if not specified, it removes the last item

my_list_o = ["i", "dont" , "like", "lists", "anymore"]
del my_list_o[2]                                              #removes the specifies index
print(my_list_o)

my_list_p = ["i", "hate","lists"]
del my_list_p                                                 #deletes the whole list

my_list_q = ["i" , "cant", "really" "explain" ,"it"]
my_list_q.clear()
print(my_list_q)                                              #list still exists, is empty

###

my_list_r = ["i", "havent", "got", "the", "words"]
for x in my_list_r:                                           #prints all items one by one
    print(x)

for i in range(len(my_list_r)):
    print(my_list_r[i])

my_list_s = ["apple", "banana", "cherry"]
i = 0
while i < len(my_list_s):
  print(my_list_s[i])
  i = i + 1

my_list_t = ["apple", "banana", "cherry"]
[print(x) for x in my_list_t]

###

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)                                               #puts words that have a in them in the new list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)                                               #simpler version

###

my_list_u = ["orange", "mango", "kiwi", "pineapple", "banana"]
my_list_u.sort()
print(my_list_u)

my_list_u = ["orange", "mango", "kiwi", "pineapple", "banana"]
my_list_u.sort(reverse = True)
print(my_list_u)

my_list_v = [100, 50, 65, 82, 23]
my_list_v.sort()
print(my_list_v)

my_list_v = [100, 50, 65, 82, 23]
my_list_v.sort(reverse = True)
print(my_list_v)

def myfunc(n):
  return abs(n - 50)

my_list_v = [100, 50, 65, 82, 23]
my_list_v.sort(key = myfunc)
print(my_list_v)

my_list_x = ["banana", "Orange", "Kiwi", "cherry"]
my_list_x.sort()
print(my_list_x)

my_list_x = ["banana", "Orange", "Kiwi", "cherry"]
my_list_x.sort(key = str.lower)
print(my_list_x)

my_list_x = ["banana", "Orange", "Kiwi", "cherry"]
my_list_x.reverse()
print(my_list_x)

###

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)                             #joins two lists


list4 = ["a", "b" , "c"]
list5 = [1, 2, 3]

for x in list5:
  list4.append(x)

print(list4)                           #also kinda? joins two lists


list6 = ["a", "b" , "c"]
list7 = [1, 2, 3]

list6.extend(list7)
print(list6)                           #also joins lists?

###