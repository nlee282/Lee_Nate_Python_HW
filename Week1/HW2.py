import random

num = random.randint(1, 9)

guess = 0

while guess!=num:
    guess = input("Enter a number: ")
    while guess.isdigit() == False:
        guess = input("Enter a number: ")
    guess = int(guess)
    if guess>num:
        print("Lower")
    elif guess<num:
        print("Higher")

print("You guessed the number!")