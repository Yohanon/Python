import random
print("Welcome to Game")
print("Enter press any key to enter don't press q or EOF ")
print("Enter q for quit")

while (True):
    choice = input("Enter your choice").lower()
    if choice == "q":
        break

    number = random.randint(1,50)
    tries = 1
    while (True):
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("You have to enter a number between 1 and 50")
            continue

        if guess == number :
            print("YOu have guessed the number congradulation")
            print(f"It took you {tries}")
            break
        elif guess > number:
            print("Try lower number")
        else:
            print("Try higher number")
        tries = tries + 1
