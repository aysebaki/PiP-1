# Task 1
#

# Run through values in the range [3, 20) and compute the sum of their squares.
# Use a for loop to solve this task.

val = 0
for i in range(3, 20):
    val += i ** 2

#
# Task 2
#

# Run through values in the range [3,20) and compute the sum of their squares.
# Use a while loop to solve this task.

val = 0
i = 3
while i < 20:
    val += i ** 2
    i += 1

#
# Task 3
#

# Run through values in the range [3,20) and print only those numbers that are
# divisible by 3 (without remainder).

for i in range(3, 20):
    if i % 3 == 0:
        print(i)

#
# Task4
#

# Create an empty sting "some_strings" and append user (console) input to this
# string until the user types "end". This last word "end" should not be appended
# to "some_strings".

print("ask about task 4")

# Task 5
#

# Use a while Loop to implement a pseudo-login scenario in which a user is asked
# to enter a password (console input). If the password is correct, print "Login
# success". Otherwise, let the user try ogoin. In case of entering three wrong
# passwords, print "Contact the administrator to recover password", The choice
# of the correct password is up to you.
password = "gabe"
user_input = input("Please enter your password: ")
tries = 0
while user_input != password:
    if tries != 2:
        user_input = input("Please try again")
        tries += 1
    else:
        print("Contact admin")
        break
else:
    print("Login successful ")

#
#Task 6
#

# Read a string from the console input. Iterate through this string ond count
# the number of digits (0-9), the number of lowercose characters and the number
# of other characters (neither digits nor lowercase characters). You can use the
# string methods "c.isdigit()" and "c. isLower()".

inp= input("Enter something")
n_digits = 0
n_lowercase = 0
n_rest = 0
for i in inp:
    if i.isdigit():
        n_digits += 1
    elif i.islower():
        n_lowercase += 1
    else:
        n_rest += 1

#
#Task 7
#

#Use a double-nested loop to iterate through both of the strings "text" and
# "chars_to_check. If the current character from "text" matches one in
# "chars_to_check", print it together with its index position in "text".

text = "some string"
#       0123456789|
#                10
#                11
chars_to_check = "aeiou"

for character in chars_to_check:
    for i, char in enumerate (text):
        if character == char:
            print("f{i} --> {char}")

