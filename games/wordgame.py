import random


def generate_word():
    try:
        choice = int(input("Enter 1 for programming related wordws, enter 2 for science related words and 3 for misc"))
        choice-= 1
    except:
        print("Enter a valid number please! ")
        generate_word()
    word = [["python","java","rust","coding","array",],["Physics","thermodynamics","calculus","entropy","anatomy"],["hello","world","linux","movie","banana","monkey","sheru"]]
    b = word[choice][random.randint(0,len(word[choice]))]
    #printing the blank word so user knows the length
    for i in range (len(b)):
       print("_",end="")
    return b


def checker(word,guess):
    a=list(word)
    guess=list(guess)
    _return= list()
    # to keep all the correct words
    for i in range(len(a)):
        if a[i]==guess[i]:
            _return.append(guess[i])
            a[i]="#"
            guess[i]="~"
        else:
            _return.append("_")
    # to check for right letters but wrong postion
    for i in guess:
        if i in a:
            _return[_return.index(i)]="*"
            guess[guess.index(i)]="~"
    return _return


def rules():
    print("A random word will be generated. You must guess it")
    print(
        "If a correct letter in correct place is entered the letter would be printed on screen"
    )
    print(
        "If a correct letter but in wrong order is entered then a star would be printed "
    )
    print("If a wrong letter is entered then a '_' will be printed")
    print("Only enter letter no special characters or numbers and also enter the right number of letters")

def main():
    print("Select and enter one of the following")
    print("Press p to play")
    print("Press r to show rules")
    print("Press q to quit ")
    ch = input("Enter your choice: ").lower

    # BLock to check which is the choice and execute
    if ch == "p" :
        word = generate_word()
        while True:

            user_guess = input("Enter your guess:").lower
            if len(user_guess) != len(word):
                print(f"Enter a same number of letters which is {len(word)}, Try again!")
                continue
            if word == user_guess:
                print("You have guessed the word congragulations")
                break
            else:
                checker(user_guess, word)
        return True
    elif ch == "r":
        rules()
        return True
    elif ch == "q" or ch == "Q" or ch == "quit":
        print("Have a great time")
        return False
    else:
        print("Invalid choice try again")


# driver
print("Welcome,", end=" ")
while True:
    a = main()
    print(
        "-------------------------------------------------------------------------------------"
    )
    if a == False:
        break
