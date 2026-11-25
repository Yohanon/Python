def collartz_stats(n: int):
    print(n, end="")
    greater = 0
    step = 0
    while n != 1:
        n = (n // 2) if (n % 2 == 0) else (3 * n + 1)
        if n > greater:
            greater = n
        step += 1
        print("-->", n, end="")
    print()
    print("Steps:", step)
    print("Peak:", greater)

    # end of function


# main function
while True:
    num = int(input("Enter a postive number: "))
    if num > 0:
        collartz_stats(num)
        break
        # end of program
    else:
        print("Enter a positive number ")
