age = int(input("Enter age"))
salary = int(input("Enter salary")) if age >18 else print()


if age <0:
    print("Invalid age")

if age <=7:
    print("Child ticket: 10 $")

if 8<= age <=17:
    print("Teenegar ticket: 15$")

if salary <0:
    print("Invalid salary")

if salary <=1000:
    print("Reduced adult ticket 1: 20$")

if 1001<= salary <=2000:
    print("Reduced adult ticket 2: 25$")

if salary >2000:
    print("Adult ticket: 30$")



