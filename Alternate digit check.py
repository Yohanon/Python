def enter():
    while True:
        try:
           return int(input("Enter a number: "))
        except ValueError:
            print("Invalid input, try again!")
# function ends

def alternate(num):
    counter = 2 if num%2==0 else 1
    num//=10
    while num>0:
        d=num%10
        if counter==2:
            if d%2==0:
                return False
            else:
                counter = 1
        else:
            if d%2==0:
                counter = 2
            else:
                return False
        num//=10
    return True 
def seperator():
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print()
# main function
operations = 0
while True:
    print("Enter one of the following")
    print("1.Entering number")
    print("2.Number of operantions done")
    print("3.Quit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice try again")
        seperator()
        continue
    if choice == 1:
        num = abs(enter())
        if (alternate(num)):
            print("The number is alternate number")
        else:
            print("The number is not an alternate number")
        operations+=1
        _=input("Please press Enter to continue")
    elif choice == 2:
        print("Number of operations are:",operations)
        _=input("Please press Enter ")
    elif choice == 3:
        print("Thank you for using our service")
        break
    else:
        print("Invalid choice try again")
    seperator()


