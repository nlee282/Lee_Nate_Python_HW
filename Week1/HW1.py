currentYear = 2024

name = input("Enter your name: ")

age = ""
while age.isdigit() == False:
    age = input("Enter your age: ")

age = int(age)

inpt = ""
while inpt!='y' and inpt!='n':
    inpt = input("Has your birthday already passed? y/n: ")

if inpt=='y':
    offset = 0
else:
    offset = -1


print(f"Hi {name}! You will turn 100 years old in {currentYear+100-age+offset}")