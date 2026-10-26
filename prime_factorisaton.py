from typing_extensions import IntVar


def count_digit(n):
    count = 0
    while(n>0):
        n//=10
        count+=1
    return count
# end of functon

def armstrong_numbers(n,digit):
    _sum = 0
    safe_num = n
    while n>0:
        b= n % 10
        _sum+= b**digit
        n//=10
    if safe_num == _sum :
        print(safe_num,end=",")
# end of functiom

# main function 
num = 0 
while (True):
    num = int(input("Enter a positive non zero number: "))
    if num<=0:
        print("Enter a positive number")
        continue
    else:
        break
# loop ends input is sorted 

for i in range (1,num+1):
    di = count_digit(i)
    armstrong_numbers(i,di)
# end of program

