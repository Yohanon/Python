import random


def generation():
    return random.randint(1, 3)

    # 1. is rock
    # 2. is scissor
    # 3. Paper


def won(com, hum):
    if com == hum :
        return "TIE"
    elif (com == 1 and hum == 2) or (com == 2 and hum == 3) or (com == 3 and hum == 1):
        return False
    else:
        return True


def main():
    while True:
        print("Enter 1 for Rock \n 2 for Scissor \n 3 for paper or press 0 for quit")
        com = generation()
        try:
            hum = int(input("Enter a number: "))
        except ValueError:
            print("Enter a valid number")
            continue
        if hum == 0:
            break
        if hum > 3 or hum < 1:
            print("Enter a number from 1 to 3 only")
        winner = won(com, hum)
        if winner == True:
            print("YOU WON")
        elif winner == False:
            print("YOU LOST")
        else:
            print("TIE")

main()
