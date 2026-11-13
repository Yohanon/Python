import random
from traceback import print_exception


def generate_word():
    word = ""
    i = 0
    for i in range(5):
        a = random.randint(65, 90)
        word = word + chr(a)
    return word


def checker(user_word, word):
    for i in range(5):
        if user_word[i] == word[i]:
            print(user_word[i], end="")
        elif user_word[i] in word:
            print("*", end="")
        else:
            print("_", end="")
    print()  # TO Shift cursor to new line


def rules():
    print("A random 5 letter string will be generated. You must guess it")
    print(
        "If a correct letter in correct place is entered the letter would be printed on screen"
    )
    print(
        "If a correct letter but in wrong order is entered then a star would be printed "
    )
    print("If a wrong letter is entered then a '_' will be printed")


def main():
    print("Select and enter one of the following")
    print("Press p to play")
    print("Press r to show rules")
    print("Press q to quit ")
    ch = input("Enter your choice: ")

    # BLock to check which is the choice and execute
    if ch == "p" or ch == "P":
        word = generate_word()
        while True:
            user_word = input("Enter your guess:")
            user_word = user_word.upper()
            if len(user_word) != 5:
                print("Enter a 5 letter word, Try again!")
                continue
            if word == user_word:
                print("You have guessed the word congragulations")
                break
            else:
                checker(user_word, word)
        return 1
    elif ch == "r" or ch == "R":
        rules()
        return 1
    elif ch == "q" or ch == "Q" or ch == "quit":
        print("Have a great time")
        return 0
    else:
        print("Invalid choice try again")


# driver
print("Welcome,", end=" ")
while True:
    a = main()
    print(
        "-------------------------------------------------------------------------------------"
    )
    if a == 0:
        break
