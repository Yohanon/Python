import random

print("Welcome to Game")
print("Enter press Enter to play ")
print("Enter q for quit")

while (True):
    try:
        choice = input("Enter your choice: ").lower()
        if choice == "q" :
            break
        elif choice != "":
            print("Invalid choice!, Please press enter key or enter q")
            continue
    except EOFError:
        break


    number = random.randint(1,50)
    tries = 1
    while (True):
        try:
            guess = int(input("Enter a number between 1 and 50: "))
        except ValueError :
            print("You have to enter a number between 1 and 50")
            continue
        if guess > 50 or guess < 0:
            print("Please enter a number between 1 and 50")
            continue

        if guess == number :
            print("YOu have guessed the number congradulation")
            print(f"It took you {tries} tries")
            break
        elif guess > number:
            print("Try lower number")
        else:
            print("Try higher number")
        tries = tries + 1
