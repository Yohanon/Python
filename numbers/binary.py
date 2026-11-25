def binary(n):
    bi = 0
    c = 0
    while n > 0:
        bi = bi + (n % 2) * (10**c)
        n //= 2
        c += 1
    return bi


def Enter():
    while True:
        num = int(input("Enter a number: "))
        if num > 255 or num < -255:
            print("Too large of a binary to store in int")
            continue
        break
    return num


# main function
num = Enter()
if num >= 0:
    bi = binary(num)
    print("The binary for", num, "is", bi)
else:
    bi = binary(abs(num))
    print("The binary for", num, "is", -1 * bi)
