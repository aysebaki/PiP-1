"File Handling, Read Files, Write/Create Files, Delete Files"

f = open("selfstudy.txt")

f = open("selfstudy.txt", "rt")         #this is the same code as the one above
                                        #"r" for read & "t" for text are default values, so we dont need to specify them

"#########################################################################################################################################"

f = open("selfstudy.txt", "r")               #r for read
print(f.read())

f = open("selfstudy.txt", "r")               #returns the first 7 characters
print(f.read(7))

f = open("selfstudy.txt", "r")               #r for read, returns lines (first one by default)
print(f.readline())

f = open("selfstudy.txt", "r")               #r for read, returns the first two lines now
print(f.readline())
print(f.readline())

f = open("selfstudy.txt", "r")              #with the looping method we can read the whole file
for x in f:
    print(x)

f = open("selfstudy.txt", "r")               #r for read, we should always close files when we're done with them
print(f.readline())
f.close()

"######################################################################################################################################"

f = open("selfstudy2.txt", "a")               #a for append, it will add to the end of the file
f.write("Now the file has more content!")
f.close()

f = open("selfstudy2.txt", "r")
print(f.read())
f.close()


f = open("selfstudy3.txt", "w")              #w for write, it overwrites existing content
f.write("Ooooops! I have deleted the whole content!")
f.close()

f = open("selfstudy3.txt", "r")             #just done to read the file after the change
print(f.read())


#earlier we just edited and read some already existing files
#we now want to create new files

#f = open("myfile.txt", "x")        #bc it returns an erros after the file is createt

f = open("myfile.txt", "w")
f.write("Hello! I just created this and it is really exiting! I'm really starting to dig this programming thing")
f.close()

#f = open("myfile.txt", "r")
#print(f.read)
#f.close()

"########################################################################################################################################"

import os
os.remove("selfstudy2.txt")           #deleting a file

if os.path.exists("selfstudy3.txt"):     #checking if the file is there and then deleting it
    os.remove("selfstudy3.txt")
else:
    print("The file does not exist")

os.rmdir("myfolder")                    #deletes an entire folder, but you can only delete empty folders

