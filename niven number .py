def niven(limit):
    for i in range(1, limit + 1):
        j = i
        _s = 0
        while j > 0:
            _s += j % 10
            j //= 10
        if i % _s == 0:
            print(i, end=" ")


# end of function

while True:
    num = int(input("Enter the upper limit: "))
    if num > 0:
        niven(num)
        break
    else:
        print("Enter a positive number non Zero number ")
# end of Loop
