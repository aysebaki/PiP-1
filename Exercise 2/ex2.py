s = input("Enter text: ")
n_uppercase = 0

for char in s:
    if char.isupper():
        n_uppercase +=1
    else:
        pass

if n_uppercase == 1:
    print("The input text contains" ,n_uppercase, "uppercase character.")
else:
    print("The input text contains" ,n_uppercase, "uppercase characters.")
