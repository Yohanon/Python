# program to find if number is palindrome
def rev(a):
    b = 0
    while a > 0:
        c = a % 10
        b = b * 10 + c
        a //= 10
    return b
    # end of function


# main function
num = int(input("Enter the number: "))
a = rev(num)  # passing the value to function

# checking if num is same
if num == a:
    print("Palindrome")
else:
    print("Not a Palindrome")
