secret_number = int(input("Enter number to guess: "))
s = True
while s is True:
    x = input("Enter number: ")
    try:
        if int(x) < secret_number:
            print("Your number is smaller.")
        if int(x) > secret_number:
            print("Your number is bigger.")
        if int(x) == secret_number:
            print("Congratulations!")
            s = False
    except:
        if str(x) == "exit":
            print("You lost!")
            s = False



